#include "fpt.h"

#define ABSORBED -999

void take_step(double* current, double* clock, double epsi_b, double epsi_d,
               double dt, gsl_rng* rng) {
    double x = *current;
    double noise = gsl_ran_gaussian_ziggurat(rng, 1.0);
    double drift_term = epsi_b * (1 - x) - epsi_d * x;
    double diff_term = sqrt(2 * x * (1 - x));
    if (drift_term == 0 && diff_term == 0) {
        *current = ABSORBED;
        return;
    }
    *current = x + drift_term * dt + diff_term * sqrt(dt) * noise;
    *clock = *clock + dt;
}

bool hit_threshold(double initial, double next, double cur, double threshold) {
    return (threshold == cur) || (initial > threshold && threshold > cur) ||
           (initial < threshold && threshold < cur) ||
           (initial == threshold && ((next > threshold && threshold > cur) ||
                                     (next < threshold && threshold < cur)));
}

void hit_reflection(double initial, double next, double* cur,
                    double* reflection, int n_reflected) {
    int i = 0;
    for (; i < n_reflected; i = i + 1) {
        if (hit_threshold(initial, next, *cur, reflection[i])) {
            *cur = reflection[i];
            return;
        }
    }
}

bool hit_absorbtion(double initial, double next, double cur, double* absorbtion,
                    int n_final) {
    int i = 0;
    for (; i < n_final; i = i + 1) {
        if (hit_threshold(initial, next, cur, absorbtion[i])) {
            return true;
        }
    }
    return false;
}

void get_passage_times(long n_samples, double max_time, double x_0, double* x_a,
                       int n_absorbing, double* x_r, int n_reflected,
                       double epsi_b, double epsi_d, double dt, int rng_seed,
                       double* output) {
    /* initialize GSL random number generator*/
    gsl_rng_env_setup();
    gsl_rng* rng = gsl_rng_alloc(gsl_rng_taus);
    long seed = (long)rng_seed;
    gsl_rng_set(rng, seed);
    /* initial global state */
    double clock = 0;
    double x = x_0;
    double x_1 = x;
    /* generate event series */
    long idx = 0;
    for (; idx < n_samples; idx += 1) {
        clock = 0;
        x = x_0;
        take_step(&x, &clock, epsi_b, epsi_d, dt, rng);
        hit_reflection(x_0, x_1, &x, x_r, n_reflected);
        x_1 = x;
        while (x != ABSORBED &&
               !hit_absorbtion(x_0, x_1, x, x_a, n_absorbing) &&
               clock < max_time) {
            take_step(&x, &clock, epsi_b, epsi_d, dt, rng);
            hit_reflection(x_0, x_1, &x, x_r, n_reflected);
        }
        if (x != ABSORBED) {
            output[idx] = clock;
            if (output[idx] > max_time) {
                output[idx] = max_time;
            }
        } else {
            idx = idx - 1;
        }
    }
    /* destroy GSL random number generator*/
    gsl_rng_free(rng);
}
