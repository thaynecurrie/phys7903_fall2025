### Due December 11

### Problem 1 Feedback (2 pts)

A.

* Rate your knowledge of Python syntax prior to starting this course (1 = no knowledge, 10 = highly proficient)
* Rate your knowledge of Python syntax at the end of this course (1 = no knowledge, 10 = highly proficient) 

B.

* Rate your knowledge of core Python packages (NumPy, SciPy, Matplotlib) prior to starting this course (1 = no knowledge, 10 = highly proficient)
* Rate your knowledge of core Python packages (NumPy, SciPy, Matplotlib) at the end of this course (1 = no knowledge, 10 = highly proficient) 

C.

* Rate your knowledge of astronomy-specific Python packages (AstroPy, AstroQuery) at the start of this course (1 = no knowledge, 10 = highly proficient)
* Rate your knowledge of astronomy-specific Python packages (AstroPy, AstroQuery) at the end of this course (1 = no knowledge, 10 = highly proficient)

D.

* Rate your knowledge of Bayesian inference/Monte Carlo methods at the start of this course (1 = no knowledge, 10 = highly proficient)
* Rate your knowledge of Bayesian inference/Monte Carlo methods at the end of this course (1 = no knowledge, 10 = highly proficient)

E.

* Which topics you would have like to have covered in this class that were not covered?
* Which, if any, topics do you feel were excessively covered?


### _Problem 2--5 (8 pts)_
(4 points extra credit possible)

These problems require combining topics we have learned in the last few weeks of class in a single example.  We will read in a file containing radial-velocity data for a system with two planets.

### Problem 2 (Reading in Data)

* Read in the file rvdat.tex using astropy functions.  
* What is the data type of each column?  What does each column represent?

### Problem 3 (Time Series)

* Create a two-panel plot: on the left is an errorbar plot of the RV signal and on the right, plot the power spectrum of these signals using the Lomb-Scargle algorithm.  Make the panels look professional: label the x and y axes, thicken the axis spines, add inward-facing minor tick marks.

* Report the two strongest periodic signals in the power spectrum from visual inspection (P1 and P2). 

* (Extra credit, 2 points: create a Python function that will _calculate_ the two strongest signals, removing repeats. hint: you will probably need to create empty lists of the periods and power, sort one of these using array slicing/indexing and do a for-loop to return only the strongest signals > than some distance away from all other signals)

### Problem 4 (Maximum-Likelihood Fitting, Markov Chain Monte Carlo)

For this problem, you need a model-generating function.  Here it is (drawn from part1 of this section's notes)

```
# Generate synthetic RV data for a planet
def rv_model(t, K, P):
    """Radial velocity model for a planet"""
    # Mean anomaly
    
    #problem will adopt t0=0, e=0, and omega=0 for simplicity
    t0=0 
    e=0  
    omega=0
    M = 2 * np.pi * (t - t0) / P
    
    # Solve Kepler's equation iteratively for eccentric anomaly E
    E = M.copy()
    for _ in range(10):
        E = M + e * np.sin(E)
    
    # True anomaly
    nu = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E/2), 
                         np.sqrt(1 - e) * np.cos(E/2))
    
    # RV
    rv = K * (np.cos(nu + omega) + e * np.cos(omega))
    return rv

def rv_model_multi(t, params):
    """Multi-planet RV model"""
    K1, P1, K2, P2 = params
    rv1 = rv_model(t, K1, P1)
    rv2 = rv_model(t, K2, P2)
    return rv1 + rv2 
```

* perform a maximum-likelihood fit to the amplitudes of the two signals (K1 and K2) and periods of the two signals (P1 and P2).  Use the visual inspection of the plots in Problem 3 and the return values for the periodic signals to guide your initial guesses.

* set up a Markov Chain Monte Carlo simulation.  Add in functions for the prior and probability following the notes.   Assume uninformative (flat) priors between two extrema for each of the 4 parameters.  Use the results of the maximum-likelihood fit and visual inspection of the plots Problem 3 to guide your limits.  

For the initial state for MCMC, assume a normal distribution centered on the maximum-likelihood value for each parameter with a width of 0.05 times that value.  I.e.
 
```
starting_position = np.random.normal(soln.x,0.05*soln.x,(nwalkers,ndim))
```

* using ``emcee``, run a MCMC simulation for 10,000 steps using 50 walkers.  This should take no more than 3 minutes on your laptop (it took 20 seconds or so on mine).


### Problem 5 (Posterior Distributions from MCMC)

* from the MCMC simulation in problem 4, plot the values of each walker vs. time step, following the notes.  Based on this plot, decide how many steps to discard as burn-in.  Calculate the auto-correlation timescale for each parameter, $\tau$.

* "get" the chain: thin the chain by half the autocorrelation timescale, discard steps that are burn-in, and flatten the chain. 
 
* using ``corner`` plot the posterior distributions for K1, P1, K2, and P2.  Label them and overplot the 16, 50, and 84 percent quantiles.

* Extra Credit (2 points): following the notes in part1 of the Bayesian_MCMC section ... use the ``emcee`` output for K1, P1, K2, and P2 to calculate the msin(i) for the planet 1 and planet 2, assuming the star is 1 solar mass.  Add these two posterior distributions to K1, P1, K2, and P2 to create a new corner plot (i.e. you will have 6 variables plotted instead of 4 as before).