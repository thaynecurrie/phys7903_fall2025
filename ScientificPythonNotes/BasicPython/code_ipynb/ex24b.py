def contrast_calc2(r_plan=1,r_au=5.2):

 #r_plan in units of Jupiter radii
 #r_au in units of au

 reflected_light_contrast=1.2e-9*(r_plan/1.0)**2*(r_au/5.2)**(-2.)

 earth_contrast=2e-10


 return reflected_light_contrast,reflected_light_contrast/earth_contrast
