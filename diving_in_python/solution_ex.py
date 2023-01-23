import csv
import os


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)

        if body_whl.strip() != '':
            whl_list = body_whl.split('x')
            self.body_width = float(whl_list[0])
            self.body_height = float(whl_list[1])
            self.body_length = float(whl_list[2])
        else:
            self.body_width, self.body_height, self.body_length = 0, 0, 0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename, 'r', encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                car_type = row[0]
                brand, photo_file_name, carrying = row[1], row[3], row[5]
                if car_type == 'car':
                    passenger_seats_count = row[2]
                    car = Car(car_type, brand, photo_file_name, carrying, passenger_seats_count)
                if car_type == 'truck':
                    body_whl = row[4]
                    car = Truck(car_type, brand, photo_file_name, carrying, body_whl)
                if car_type == 'spec_machine':
                    extra = row[6]
                    car = SpecMachine(car_type, brand, photo_file_name, carrying, extra)
                try:
                    car_list.append(car)
                except UnboundLocalError as err:
                    pass
            except IndexError as err:
                pass

    return car_list


# print(get_car_list('test.csv'))
