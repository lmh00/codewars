def get_neighbourhood(n_type, mat, coordinates):
    for m in coordinates:
        print("")


N = 5
M = 5
mat = [[j+i*N for j in range (N)] for i in range(M)]

indexes1=(1,1)
expected_moore_1=[1,0,2,5,7,10,11,12]
expected_von_neumann_1=[1,5,7,11]
get_neighbourhood('moore',mat,indexes1)), sorted(expected_moore_1))
get_neighbourhood('von_neumann',mat,indexes1)), sorted(expected_von_neumann_1))

indexes2=(0,0)
expected_moore_2=[1,6,5]
expected_von_neumann_2=[1,5]
test.assert_equals(sorted(get_neighbourhood('moore',mat,indexes2)), sorted(expected_moore_2))
test.assert_equals(sorted(get_neighbourhood('von_neumann',mat,indexes2)), sorted(expected_von_neumann_2))
