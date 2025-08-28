def contrast_calc(r_plan=1,r_au=5.2):

 #r_plan in units of Jupiter radii
 #r_au in units of au

 reflected_light_contrast=1.2e-9*(r_plan/1.0)**2*(r_au/5.2)**(-2.)


 return reflected_light_contrast
