# . После.проведения.публичных.опросов.с.целью.выбора.имени.появились:.ан- глийская. подводная. лодка. B
# oaty. McBoatface,. австралийская. беговая. лошадь. Horsey. McHorseface. и. шведский. поезд. Trainy.
# McTrainface..
# Используйте. фор- матирование.с.символом.%.
# для.того,.чтобы.вывести.на.экран.победившие.имена. для.утки,.тыквы.и.шпица.

candidates = ['duck','gourd', 'spitz']
for c in candidates:
    name = c.capitalize()
    print("%sy Mc%sface" % (name,name))

