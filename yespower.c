#include "yespower.h"
/* 
 * yespower for resistance
 */
int yespower_hash(const char *input, char *output)
{
	yespower_params_t params = {YESPOWER_1_0, 4096, 32, NULL, 0};
	return yespower_tls(input, 80, &params, (yespower_binary_t *) output);
}

