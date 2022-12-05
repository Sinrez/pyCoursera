from matplotlib import pyplot as plt


class VehicleSimpleDynamic:
    def __init__(self, mass, k_b, rotorCount, accInit, velInit, posInit):
        '''
        :param mass: масса аппарата
        :type mass: float
        :param k_b: коэффициент тяги двигателя
        :type k_b: float
        :param rotorCount: количество двигателей в системе
        :type rotorCount: int
        :param accInit: начальное значение ускорения ЛА
        :type accInit: float
        :param velInit: начальное значение скорости ЛА
        :type velInit: float
        :param posInit: начальное значение положения ЛА
        :type posInit: float
        '''
        self.mass = mass
        self.k_b = k_b
        self.rotorCount = rotorCount
        self.acceleration = accInit
        self.velocity = velInit
        self.position = posInit
        # Величина ускорения свободного падения
        self.g = 9.81

    def rightParts(self, rotorsAngularVel):
        '''
        :param rotorsAngularVel: угловая скорость двигателей
        :type rotorsAngularVel: float
        '''
        # Для всех двигателей рассчитаем суммарную тягу
        rotorsAngularVelSum = 0
        for i in range(self.rotorCount):
            # суммируем квадрат заданной угловой скорости для всех двигателей
            rotorsAngularVelSum += rotorsAngularVel**2
        # Вычисляем ускорение нашей системы.
        # Получаем силу тяги создаваемую всеми двигателями
        # согласно нашей математической модели Fтяги = Kb * omega^2
        # После для получения текущего ускорения разделим полученное значение
        # на массу и вычтем ускорение свободного падения действующие на аппарат
        self.acceleration = (
            self.k_b * rotorsAngularVelSum) / self.mass - self.g

    def integrate(self, dt):
        '''
        :param dt: шаг моделирования
        :type dt: float
        '''
        # интегрируем ускорение методом эйлера
        self.velocity += self.acceleration * dt
        # Полученную скорость интегрируем для определения местоположения
        self.position += self.velocity * dt

    def calculatePosition(self, u, dt):
        '''
        :param u: управляющие воздействие
        :type u: float
        :param dt: шаг моделирования
        :type dt: float
        '''
        # Для определения положения вызываем метод для правых частей(то есть наших приращений от перемещения)
        # В данном случае приращением выступает ускорение нашей системы.
        # Для следования заданному целевому значению высоты передаем в метод наше управляющие воздействие u,
        # которое характеризует необходимую угловую скорость двигателей.
        self.rightParts(u)
        # Далее вызываем метод интегрирования
        # Интегрируем полученное при помощи функции правых частей ускорение и получаем скорость,
        # после интегрируем скорость и получаем положение.
        self.integrate(dt)

    def getPosition(self):
        '''
        :return: положение ЛА
        :rtype: float
        '''
        return self.position

    def getVelocity(self):
        '''
        :return: скорость ЛА
        :rtype: float
        '''
        return self.velocity

    def getAcceleration(self):
        '''
        :return: ускорение
        :rtype: float
        '''
        return self.acceleration


class ControlSystem():
    def __init__(self, k_p, k_i, k_d, controlLimit):
        '''
        :param k_p: коэффициент П регулятора
        :type k_p: float
        :param k_i: коэффициент И регулятора
        :type k_i: float
        :param k_d: коэффициент Д регулятора
        :type k_d: float
        :param controlLimit: ограничение по управляющему воздействию
        :type controlLimit: float
        '''
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d
        self.desiredPosition = 0
        self.error = 0
        self.errorPast = 0
        self.integral = 0
        self.controlLimit = controlLimit

    def setDesiredPosition(self, desiredPosition):
        '''
        :param desiredPosition: целевое положение ЛА
        :type desiredPosition: float
        '''
        # данный метод устанавливает целевое положение ЛА,
        # к которому система с течением времени будет стремиться(в нашем примере это высота)
        self.desiredPosition = desiredPosition

    def PID(self, currentPosition, dt):
        '''
        :param currentPosition: текущее положение ЛА
        :type currentPosition: float
        :param dt: шаг моделирования
        :type dt: float
        '''
        # Вычислим функцию ошибки
        self.error = self.desiredPosition - currentPosition
        # Вычисляем интеграл ошибки
        self.integral += self.error * dt
        # Получим рассчетную управляющую угловую скорость двигателей при помощи ПИД регулятора
        u = self.k_p * self.error + self.k_i * self.integral + \
            self.k_d * ((self.error - self.errorPast) / dt)
        # Установим предыдущую ошибку для использования в дальнейших итерациях
        self.errorPast = self.error
        # Вызовем звено насыщения для ограничения максимального управляющего воздействия
        u = self.saturation(u)
        return u

    def saturation(self, inputVal):
        '''
        :param inputVal: входное значение
        :type inputVal: float
        :return: выходное значение после прохождения проверки на ограничение
        :rtype: float
        '''
        # Звено насыщения ограничивает размер входного параметра
        # На выходе метода,абсолютное значение не может быть больше
        # заданного предела controlLimit
        if inputVal > self.controlLimit:
            inputVal = self.controlLimit
        elif inputVal < -self.controlLimit:
            inputVal = - self.controlLimit

        return inputVal


class Simulator():

    def __init__(self, Tend, dt, controlSys, dynamicModel):
        '''
        :param Tend: конечное время моделирования
        :type Tend: float
        :param dt: шаг моделирования
        :type dt: float
        :param controlSys: объект системы управления высотой ЛА
        :type controlSys: ControlSystem
        :param dynamicModel: объект модели ЛА
        :type dynamicModel: VehicleSimpleDynamic
        '''
        self.dt = dt
        self.Tend = Tend
        self.controlSys = controlSys
        self.dynamicModel = dynamicModel
        self.accList = []
        self.velList = []
        self.posList = []
        self.timeList = []

    def runSimulation(self):
        '''
       метод запускает моделирование системы от 0 до конечного времени Tend
       с шагом dt
        '''
        # Задаем 0 время и начинаем рассчет до тех пор пока
        # время не достигнет конечного значения Tend
        time = 0
        while (time <= self.Tend):
            # получаем положение ЛА
            pose = self.dynamicModel.getPosition()
            # Получаем скорость ЛА
            vel = self.dynamicModel.getVelocity()
            # Получаем ускорение ЛА
            acc = self.dynamicModel.getAcceleration()
            # Записываем полученные значения в списки
            # для дальнейшего построения графиков
            self.posList.append(pose)
            self.velList.append(vel)
            self.accList.append(acc)
            # self.timeList.append(time)

            # рассчитываем новое управляющие воздействие
            # на основе текущего положения(pose) ЛА
            u = self.controlSys.PID(pose, self.dt)
            # Рассчитываем положение ЛА с учетом полученного
            # управляющего воздействия
            self.dynamicModel.calculatePosition(u, self.dt)
            # увеличиваем время на dt, то есть на шаг моделирования
            time += self.dt

    def showPlots(self):
        '''
        метод строит графики на основе измерений полученных в
        ходе моделирования системы
        '''
        f = plt.figure(constrained_layout=True)
        gs = f.add_gridspec(3, 5)
        ax1 = f.add_subplot(gs[0, :-1])
        ax1.plot(self.posList)
        ax1.grid()
        ax1.set_title('position')

        ax2 = f.add_subplot(gs[1, :-1])
        ax2.plot(self.velList, "g")
        ax2.grid()
        ax2.set_title('velocity')

        ax3 = f.add_subplot(gs[2, :-1])
        ax3.plot(self.accList, "r")
        ax3.grid()
        ax3.set_title('acceleration')

        plt.show()


'''
 Объявим параметры для моделирования
'''
k_p = 305 #коэффициент Пропорционального регулирования
k_i = 70 #коэффициент Интегрального регулирования
k_d = 180 #коэффициент Дифференциального регулирования
dt = 0.01 # шаг моделирования системы (например одна сотая секунды)

Tend = 20 # конечное время моделирования (например 20 сек)

# Масса ЛА
mass = 0.006
# Коэффициент тяги двигателя ЛА
k_b = 3.9865e-08
# Количество двигателей ЛА
rotorCount = 4
# Ограничение на угловую скорость двигателей рад/сек
motorSpeedLimit = 1000

'''
Создадим объект контроллера и объект для нашей математической модели
'''
controller = ControlSystem(k_p, k_i, k_d, motorSpeedLimit)
uavSimpleDynamic = VehicleSimpleDynamic(mass, k_b, rotorCount, 0, 0, 0)
'''
Установим целевое положение для нашей системы
'''
controller.setDesiredPosition(10)


"""
Создадим объект симулятора и передадим в него контроллер
 и математическую модель
"""
sim = Simulator(Tend, dt, controller, uavSimpleDynamic)
sim.runSimulation()  # запуск симулятора
sim.showPlots()  # построение графиков