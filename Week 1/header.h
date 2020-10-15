#ifndef SEAN_TEST_1
#define SEAN_TEST_1
class vecsim {
public:
	vecsim(double* v1, double* v2, int v_len);
	vecsim();
	
	double Euclidean();
	double Euclidean(double* v1, double* v2, int v_len);
	double Cosine();
	double Cosine(double* v1, double* v2, int v_len);
private:
	double* vec1, *vec2;
	int vec_len;
};

#endif // !SEAN_TEST_1