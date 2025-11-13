## Homework 8 - Week 13 (due November 25)
### NOTE !!! there will be one more HW assignment that will cover some stuff in AstroPy + remainder of course content (e.g. MCMC)


### 1. Project Update 

* Please give me a **short** update on the progress of your class project.  In particular, I would like to see ...

- A description of the current status of your project
- Items where you are getting stuck (if any)/questions you may have
- Any plots or graphics you have produced beyond those from the prior homework.

### 2. Reading in Fits Files

* read in 'keckimage.fits' in /code/sect1/files/
* save the image array as a variable, save the header as a variable
* from the header, return the keyword values for the altitude and azimuth of the telescope during this exposure
* use i) use the .info() call we talked about in the lecture to display a value for the dimensions of the iamge, ii) use a NumPy function call to return a value for the dimensions of the image

### 3. Reading in Fits Files, Writing Fits Files

* read in the data cube `adi_oct172021.fits' in /code/sect1/files/
* return the keyword value for aperture radius in the third slice (here the 0th slice is indexed as 0, 1st slice is indexed as 1, etc)
* compute the pixel value of the cube at for the 10th slice at x=82, y=79.  
* What are the flux density units of the cube?
* take the median of 'adi_oct172021.fits' across all wavelengths
* save as a new fits file called ``median_adi_oct172021.fits`` with _all_ the previous fits header information retained.

Note: all numbers listed above -- i.e. the slice number, spatial pixel numbers x and y -- are indexed from 0, not 1.

### 4. Animations

Start with the animation ``ex1_6.gif`` and ``ex1_6.mp4`` described in the lecture note section on animations and located in /code/sect1/files/. 

 Edit the source code to create a gif or a mpeg movie that prints a) a label at the top-left saying ``Exoplanet HIP 99770 b`` on the top line and ``SCExAO/CHARIS`` on the second line and a counter at the bottom-left reading ``Wavelength Slice [Number]`` where the number increments by 1 with each slice.  See the attached file ``problem3.mp4`` for an example.
 
 Save your file as ``new_exoplanet_animation.mp4`` or ``new_exoplanet_animation.gif``
 
 Hints:
 
 * with each frame in the animation the original source code in my notes appends ``im`` which is an ``axes.imshow`` call (i.e. appends an image frame).   To get markups added, you also need to append them with each loop.
 
 * think carefully about _where_ you add the wavelength labeling in your source code.

 
### 5. AstroPy Tables

* read in the file ``leggett.txt`` (data for brown dwarfs from my colleague at the Gemini Observatory, Sandy Leggett).  It is located in /code/sect2/files/.

* what is the format type for this table? (basic, latex, mrt, csv, or ipac)

* one of the columns is the **negative** of the distance modulus ``M-m``: ``-5*log10(distance/10)``, where distance is in parsecs.  The others are self-explanatory

Create a new table in the LaTeX format called ``newleggett.tex`` with the columns 'Name', 'Distance', 'H mag', and 'abs Hmag'.   Here 'distance', should be the distance in parsecs (you can figure out out from the distance modulus) and 'abs Hmag' is the absolute H band magnitude (i.e. absolute magnitude = apparent magnitude - distance modulus).

* read your newly-created table back in to confirm that you have formatted the table properly.  If you do this in Jupyter Notebooks, the new table should be displayed as follows:

![](./newtable_screenshot.png)

### 6. Units

* take the result from ``newleggett.tex``.  Read in this file using ``ascii.read``, extract the column for Distance in units of parsecs.
* use ``units`` to give explicit units of parsecs to these distances.  
* using ``units``, convert these distances to light-years (abbreviated ``lyr``).
* Do a simple histogram plot following the format of our galaxy velocity dispersion example:

![](./distance_hist.png)

### 7. Astrometry and Photometry with Photutils 

The file "star_nopsfsub.fits" is an unsaturated image of the star (which should be in the middle of the image).  The file "psfsub.fits" is the same image with the stellar halo removed to flatten the background and reveal a planet-mass companion nearly due-west of the star (it's at an x position of about 320).

Assume that the pixel scale is roughly 9.952 milliarcseconds/pixel and that the image is rotated perfectly north-up, east-left.

* read in this file using astropy functions

* using photutils, compute the centroid of the planet-mass companion's position in pixel values (x and y).   Then, given the pixel scale, compute its position in arc-seconds in units [East, North] _relative_ to the star. 

    (again, the image is north-up, east-left: so objects east of the star will have a negative x value and vice versa. If its position were 0.5 arcseconds east and -0.7 arcseconds south of the star then you would report this as [East, North] = [0.5,-0.7]).
 
### 8. Photometry with Photutils (+ 2 possible extra credit point)
    
* using photutils, plot the radial-profile of the star.  Find where the star's brightness roughly (emphasis on **roughly**!) decreases to about half its peak value: round up to the nearest integer and set this value to be the aperture radius.


* Compute photometry of the star (from "nopsfsub" and the companion (from "psfsub") with this aperture radius both in units of counts.  Then compute the contrast between the star and the planet in units of magnitudes (note: do not overthink this: it's as simple as it sounds).


Hints: 

* to figure out a good initial guess for the centroid positions, try doing the extra credit part by displaying the image using Matplotlib: the notes give a good recipe for how to do this.

* look at the notes on photutils VERY closely to figure out how to plot the radial profile.   The answer for the half-peak value will be in between two integers: again, round up to get the aperture radius you should use.
* you do not need to compute astrometric errors or photometric errors


**Extra Credit** (2 points)

- Display the image as shown below
 ![](./planetdiscovery.png) (1 point)


 
- What is the name of this planet? (1 point)
