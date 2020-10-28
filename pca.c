#include <stdlib.h>

//2D PCA
void getPCAeval(const int pcaLen, const double *x_vec, const double *y_vec, double *eval, double **evec){
	
	double sumX = 0; double sumY = 0;
	for (int i = 0; i < pcaLen; ++i)
	{
		sumX += x_vec[i]; sumY += y_vec[i];
	}

	double meanX = sumX / pcaLen; double meanY = sumY / pcaLen;

	//PCA covairance matrix 
	double sumXX = 0; double sumXY = 0; //sumXY = sumYX
	double sumYY = 0;
	for (int i=0; i < pcaLen; i++) {
		sumXX += (x_vec[i] - meanX) * (x_vec[i] - meanX); 
		sumXY += (x_vec[i] - meanX) * (y_vec[i] - meanY);
		sumYY += (y_vec[i] - meanY) * (y_vec[i] - meanY);
	}

	double cXX = sumXX / (pcaLen - 1); 
	double cXY = sumXY / (pcaLen - 1);
	double cYY = sumYY / (pcaLen - 1);

	double a = 1; double b = (-1)*(cXX + cYY); double c =  cXX*cYY - cXY*cXY;
	//Fisrt eigenvalue, lambda+
	eval[0] = ((-1)*b + sqrt(pow(b,2) - 4*a*c) ) / (2*a);
	//Second eigenvalue, lambda-	
	eval[1] = ((-1)*b - sqrt(pow(b,2) - 4*a*c) ) / (2*a);

	for (int i = 0; i < 2; ++i)
	{
		evec[i][0] = -cXY;
		evec[i][1] = cXX -eval[i];
	}

}
