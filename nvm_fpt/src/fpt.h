#include <gsl/gsl_randist.h>
#include <gsl/gsl_rng.h>
#include <math.h>
#include <stdbool.h>

/**
 * This function generates a sample of first passage (absorption) times for the
 * voter model with specified parameters and boundary conditions. One of the
 * boundaries ought to absorbing, while another might be reflective or
 * absorbing. If both boundary conditions are absorbing, both absorption events
 * count as passage events.
 *
 * Simulation is conducted by numerically solving respective stochastic
 * differential equation. Numerical simulation relies on Euler-Maruyama method.
 *
 * Function arguments:
 * @param n_samples    The number of absorption events to generate.
 * @param max_time     The maximum duration to sample.
 * @param x_0          The initial condition for the model.
 * @param x_a          Array of absorbing boundary locations.
 * @param n_absorbing  The number of absorbing boundaries specified in `x_a`.
 * @param x_r          Array of reflecting boundary locations.
 * @param n_reflected  The number of reflecting boundaries specified in `x_r`.
 * @param epsi_b       0->1 transition (birth) rate of the voter model.
 * @param epsi_d       1->0 transition (death) rate of the voter model.
 * @param dt           The time step for the numerical simulation method.
 * @param rng_seed     Seed for the random number generator for reproducibility.
 * @param output       Pre-allocated array to store the simulation outputs.
 *                     The array must be at least `n_samples` long.
 */
extern void get_passage_times(long n_samples, double max_time, double x_0,
                              double* x_a, int n_absorbing, double* x_r,
                              int n_reflected, double epsi_b, double epsi_d,
                              double dt, int rng_seed, double* output);
