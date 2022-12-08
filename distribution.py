def normal_01_cdf_inv ( cdf ):
  import numpy as np

  a = np.array ( [ \
    3.3871328727963666080,      1.3314166789178437745e+2, \
    1.9715909503065514427e+3,   1.3731693765509461125e+4, \
    4.5921953931549871457e+4,   6.7265770927008700853e+4, \
    3.3430575583588128105e+4,   2.5090809287301226727e+3 ] )
  b = np.array ( [ \
    1.0,                        4.2313330701600911252e+1, \
    6.8718700749205790830e+2,   5.3941960214247511077e+3, \
    2.1213794301586595867e+4,   3.9307895800092710610e+4, \
    2.8729085735721942674e+4,   5.2264952788528545610e+3 ] )
  c = np.array ( [ \
    1.42343711074968357734,     4.63033784615654529590, \
    5.76949722146069140550,     3.64784832476320460504, \
    1.27045825245236838258,     2.41780725177450611770e-1, \
    2.27238449892691845833e-2,  7.74545014278341407640e-4 ] )
  const1 = 0.180625
  const2 = 1.6
  d = np.array ( [ \
    1.0,                        2.05319162663775882187,    \
    1.67638483018380384940,     6.89767334985100004550e-1, \
    1.48103976427480074590e-1,  1.51986665636164571966e-2, \
    5.47593808499534494600e-4,  1.05075007164441684324e-9 ] )
  e = np.array ( [ \
    6.65790464350110377720,     5.46378491116411436990,    \
    1.78482653991729133580,     2.96560571828504891230e-1, \
    2.65321895265761230930e-2,  1.24266094738807843860e-3, \
    2.71155556874348757815e-5,  2.01033439929228813265e-7 ] )
  f = np.array ( [ \
    1.0,                        5.99832206555887937690e-1, \
    1.36929880922735805310e-1,  1.48753612908506148525e-2, \
    7.86869131145613259100e-4,  1.84631831751005468180e-5, \
    1.42151175831644588870e-7,  2.04426310338993978564e-15 ] )
  huge = np.finfo(float).max
  split1 = 0.425
  split2 = 5.0

  if ( cdf <= 0.0 ):
    value = - huge
    return value

  if ( 1.0 <= cdf ):
    value = huge
    return value

  q = cdf - 0.5

  if ( abs ( q ) <= split1 ):

    r = const1 - q * q
    value = q * r8poly_value_horner ( 7, a, r ) \
              / r8poly_value_horner ( 7, b, r )

  else:

    if ( q < 0.0 ):
      r = cdf
    else:
      r = 1.0 - cdf

    if ( r <= 0.0 ):

      value = huge

    else:

      r = np.sqrt ( - np.log ( r ) )

      if ( r <= split2 ):

        r = r - const2
        value = r8poly_value_horner ( 7, c, r ) \
              / r8poly_value_horner ( 7, d, r )

      else:

         r = r - split2
         value = r8poly_value_horner ( 7, e, r ) \
               / r8poly_value_horner ( 7, f, r )

    if ( q < 0.0 ):
      value = - value

  return value

def normal_01_cdf ( x ):
  import numpy as np

  a1 = 0.398942280444
  a2 = 0.399903438504
  a3 = 5.75885480458
  a4 = 29.8213557808
  a5 = 2.62433121679
  a6 = 48.6959930692
  a7 = 5.92885724438
  b0 = 0.398942280385
  b1 = 3.8052E-08
  b2 = 1.00000615302
  b3 = 3.98064794E-04
  b4 = 1.98615381364
  b5 = 0.151679116635
  b6 = 5.29330324926
  b7 = 4.8385912808
  b8 = 15.1508972451
  b9 = 0.742380924027
  b10 = 30.789933034
  b11 = 3.99019417011
#
#  |X| <= 1.28.
#
  if ( abs ( x ) <= 1.28 ):

    y = 0.5 * x * x

    q = 0.5 - abs ( x ) * ( a1 - a2 * y / ( y + a3 \
      - a4 / ( y + a5 \
      + a6 / ( y + a7 ) ) ) )
#
#  1.28 < |X| <= 12.7
#
  elif ( abs ( x ) <= 12.7 ):

    y = 0.5 * x * x

    q = np.exp ( - y ) \
      * b0  / ( abs ( x ) - b1 \
      + b2  / ( abs ( x ) + b3 \
      + b4  / ( abs ( x ) - b5 \
      + b6  / ( abs ( x ) + b7 \
      - b8  / ( abs ( x ) + b9 \
      + b10 / ( abs ( x ) + b11 ) ) ) ) ) )
#
#  12.7 < |X|
#
  else:

    q = 0.0
#
#  Take account of negative X.
#
  if ( x < 0.0 ):
    value = q
  else:
    value = 1.0 - q

  return value

def normal_01_cdf_values ( n_data ):
  import numpy as np

  n_max = 17

  f_vec = np.array ( (\
     0.5000000000000000E+00, \
     0.5398278372770290E+00, \
     0.5792597094391030E+00, \
     0.6179114221889526E+00, \
     0.6554217416103242E+00, \
     0.6914624612740131E+00, \
     0.7257468822499270E+00, \
     0.7580363477769270E+00, \
     0.7881446014166033E+00, \
     0.8159398746532405E+00, \
     0.8413447460685429E+00, \
     0.9331927987311419E+00, \
     0.9772498680518208E+00, \
     0.9937903346742239E+00, \
     0.9986501019683699E+00, \
     0.9997673709209645E+00, \
     0.9999683287581669E+00 ))

  x_vec = np.array ((\
     0.0000000000000000E+00, \
     0.1000000000000000E+00, \
     0.2000000000000000E+00, \
     0.3000000000000000E+00, \
     0.4000000000000000E+00, \
     0.5000000000000000E+00, \
     0.6000000000000000E+00, \
     0.7000000000000000E+00, \
     0.8000000000000000E+00, \
     0.9000000000000000E+00, \
     0.1000000000000000E+01, \
     0.1500000000000000E+01, \
     0.2000000000000000E+01, \
     0.2500000000000000E+01, \
     0.3000000000000000E+01, \
     0.3500000000000000E+01, \
     0.4000000000000000E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def normal_01_mean ( ):

  value = 0.0

  return value

def normal_01_moment ( order ):
  from scipy.special import factorial2

  if ( ( order % 2 ) == 0 ):
    value = factorial2 ( order - 1 )
  else:
    value = 0.0

  return value

def normal_01_pdf ( x ):
  import numpy as np

  value = np.exp ( - 0.5 * x * x ) / np.sqrt ( 2.0 * np.pi )

  return value

def normal_01_variance ( ):
  value = 1.0

  return value

def normal_ms_cdf_inv ( cdf, mu, sigma ):
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'normal_ms_cdf_inv - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'normal_ms_cdf_inv - Fatal error!' )

  y = normal_01_cdf_inv ( cdf )

  value = mu + sigma * y

  return value

def normal_ms_cdf ( x, mu, sigma ):
y = ( x - mu ) / sigma

  value = normal_01_cdf ( y )

  return value

def normal_ms_mean ( mu, sigma ):
  value = mu

  return value

def normal_ms_moment_central ( order, mu, sigma ):
  from scipy.special import factorial2

  if ( ( order % 2 ) == 0 ):
    value = factorial2 ( order - 1 ) * sigma ** order
  else:
    value = 0.0

  return value

def normal_ms_moment_central_values ( order, mu, sigma ):
  if ( order == 0 ):
    value = 1.0
  elif ( order == 1 ):
    value = 0.0
  elif ( order == 2 ):
    value = sigma ** 2
  elif ( order == 3 ):
    value = 0.0
  elif ( order == 4 ):
    value = 3.0 * sigma ** 4
  elif ( order == 5 ):
    value = 0.0
  elif ( order == 6 ):
    value = 15.0 * sigma ** 6
  elif ( order == 7 ):
    value = 0.0
  elif ( order == 8 ):
    value = 105.0 * sigma ** 8
  elif ( order == 9 ):
    value = 0.0
  elif ( order == 10 ):
    value = 945.0 * sigma ** 10
  else:
    print ( '' )
    print ( 'normal_ms_moment_central_values - Fatal error!' )
    print ( '  Only ORDERS 0 through 8 are available.' )
    raise Exception ( 'normal_ms_moment_central_values - Fatal error!' )

  return value

def normal_ms_moment ( order, mu, sigma ):
  from scipy.special import comb
  from scipy.special import factorial2

  j_hi = ( order // 2 )

  value = 0.0
  for j in range ( 0, j_hi + 1 ):
    value = value \
      + comb ( order, 2 * j ) \
      * factorial2 ( 2 * j - 1 ) \
      * mu ** ( order - 2 * j ) * sigma ** ( 2 * j )

  return value

def normal_ms_moment_values ( order, mu, sigma ):
if ( order == 0 ):
    value = 1.0
  elif ( order == 1 ):
    value = mu
  elif ( order == 2 ):
    value = mu ** 2 + sigma ** 2
  elif ( order == 3 ):
    value = mu ** 3 + 3.0 * mu * sigma ** 2
  elif ( order == 4 ):
    value = mu ** 4 + 6.0 * mu ** 2 * sigma ** 2 + 3.0 * sigma ** 4
  elif ( order == 5 ):
    value = mu ** 5 + 10.0 * mu ** 3 * sigma ** 2 + 15.0 * mu * sigma ** 4
  elif ( order == 6 ):
    value = mu ** 6 + 15.0 * mu ** 4 * sigma ** 2 + 45.0 * mu ** 2 * sigma ** 4 \
      + 15.0 * sigma ** 6
  elif ( order == 7 ):
    value = mu ** 7 + 21.0 * mu ** 5 * sigma ** 2 + 105.0 * mu ** 3 * sigma ** 4 \
      + 105.0 * mu * sigma ** 6
  elif ( order == 8 ):
    value = mu ** 8 + 28.0 * mu ** 6 * sigma ** 2 + 210.0 * mu ** 4 * sigma ** 4 \
      + 420.0 * mu ** 2 * sigma ** 6 + 105.0 * sigma ** 8
  else:
    print ( '' )
    print ( 'normal_ms_moment_values - Fatal error!' )
    print ( '  Only ORDERS 0 through 8 are available.' )
    raise Exception ( 'normal_ms_moment_values - Fatal error!' )

  return value

def normal_ms_pdf ( x, mu, sigma ):
  import numpy as np

  value = np.exp ( - 0.5 * ( ( x - mu ) / sigma ) ** 2 ) \
    / np.sqrt ( 2.0 * np.pi * sigma ** 2 )

  return value

def normal_ms_sample ( mu, sigma ):
  import numpy as np

  y = np.random.normal ( )
 
  value = mu + sigma * y

  return value

def normal_ms_variance ( mu, sigma ):

  value = sigma * sigma

  return value

def r8_mop ( i ):
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8poly_print ( m, a, title ):
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
  print ( '' )

  if ( a[m] < 0.0 ):
    plus_minus = '-'
  else:
    plus_minus = ' '

  mag = abs ( a[m] )

  if ( 2 <= m ):
    print ( '  p(x) = %c %g * x^%d' % ( plus_minus, mag, m ) )
  elif ( m == 1 ):
    print ( '  p(x) = %c %g * x' % ( plus_minus, mag ) )
  elif ( m == 0 ):
    print ( '  p(x) = %c %g' % ( plus_minus, mag ) )

  for i in range ( m - 1, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( 2 <= i ):
        print ( '         %c %g * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '         %c %g * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '         %c %g' % ( plus_minus, mag ) )

def r8poly_value_horner ( m, c, x ):
  value = c[m]
  for i in range ( m - 1, -1, -1 ):
    value = value * x + c[i]

  return value

def r8vec_linspace ( n, a, b ):
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):
     x[i] = ( ( n - 1 - i ) * a \
            + (         i ) * b ) \
            / ( n - 1     )
 
  return x

def r8vec_print ( n, a, title ):
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_variance ( n, a ):
  import numpy as np
#
#  DDOF = 1 requests normalization by N-1 rather than N.
#
  value = np.var ( a, ddof = 1 )

  return value

def timestamp ( ):
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def truncated_normal_ab_cdf_inv ( cdf, mu, sigma, a, b ):
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'truncated_normal_ab_cdf_inv - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'truncated_normal_ab_cdf_inv - Fatal error!' )

  alpha = ( a - mu ) / sigma
  beta = ( b - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  xi_cdf = ( beta_cdf - alpha_cdf ) * cdf + alpha_cdf
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x

def truncated_normal_ab_cdf ( x, mu, sigma, a, b ):
  if ( x < a ):
  
    value = 0.0
    
  elif ( x <= b ):
  
    alpha = ( a - mu ) / sigma
    beta = ( b - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = normal_01_cdf ( alpha )
    beta_cdf = normal_01_cdf ( beta )
    xi_cdf = normal_01_cdf ( xi )

    value = ( xi_cdf - alpha_cdf ) / ( beta_cdf - alpha_cdf )
    
  else:
  
    value = 1.0

  return value

def truncated_normal_ab_cdf_values ( n_data ):
  import numpy as np

  n_max = 11

  a_vec = np.array ( ( \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0 ))

  b_vec = np.array ( ( \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0 ))

  f_vec = np.array ( ( \
    0.3371694242213513, \
    0.3685009225506048, \
    0.4006444233448185, \
    0.4334107066903040, \
    0.4665988676496338, \
    0.5000000000000000, \
    0.5334011323503662, \
    0.5665892933096960, \
    0.5993555766551815, \
    0.6314990774493952, \
    0.6628305757786487 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, a, b, x, f

def truncated_normal_ab_mean ( mu, sigma, a, b ):
  alpha = ( a - mu ) / sigma
  beta = ( b - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = normal_01_pdf ( beta )

  value = mu + sigma * ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf )

  return value

def truncated_normal_ab_moment ( order, mu, sigma, a, b ):

  from scipy.special import comb

  if ( order < 0 ):
    print ( '' )
    print ( 'truncated_normal_ab_moment - Fatal error!' )
    print ( '  ORDER < 0.' )
    raise Exception ( 'truncated_normal_ab_moment - Fatal error!' )

  if ( sigma <= 0.0 ):
    print ( '' )
    print ( 'truncated_normal_ab_moment - Fatal error!' )
    print ( '  SIGMA <= 0.0.' )
    raise Exception ( 'truncated_normal_ab_moment - Fatal error!' )

  if ( b <= a ):
    print ( '' )
    print ( 'truncated_normal_ab_moment - Fatal error!' )
    print ( '  B <= A.' )
    raise Exception ( 'truncated_normal_ab_moment - Fatal error!' )

  a_h = ( a - mu ) / sigma
  a_pdf = normal_01_pdf ( a_h )
  a_cdf = normal_01_cdf ( a_h )

  if ( a_cdf == 0.0 ):
    print ( '' )
    print ( 'truncated_normal_ab_moment - Fatal error!' )
    print ( '  PDF/CDF ratio fails, because A_cdf is too small.' )
    print ( '  A_pdf = %g' % ( a_pdf ) )
    print ( '  A_cdf = %g' % ( a_cdf ) )
    raise Exception ( 'truncated_normal_ab_moment - Fatal error!' )

  b_h = ( b - mu ) / sigma
  b_pdf = normal_01_pdf ( b_h )
  b_cdf = normal_01_cdf ( b_h )

  if ( b_cdf == 0.0 ):
    print ( '' )
    print ( 'truncated_normal_ab_moment - Fatal error!' )
    print ( '  PDF/CDF ratio fails, because B_cdf too small.' )
    print ( '  B_pdf = %g' % ( b_pdf ) )
    print ( '  B_cdf = %g' % ( b_cdf ) )
    raise Exception ( 'truncated_normal_ab_moment - Fatal error!' )

  value = 0.0
  irm2 = 0.0
  irm1 = 0.0

  for r in range ( 0, order + 1 ):

    if ( r == 0 ):
      ir = 1.0
    elif ( r == 1 ):
      ir = - ( b_pdf - a_pdf ) / ( b_cdf - a_cdf )
    else:
      ir = ( r - 1 ) * irm2 \
        - ( b_h ** ( r - 1 ) * b_pdf - a_h ** ( r - 1 ) * a_pdf ) \
        / ( b_cdf - a_cdf )

    value = value + comb ( order, r ) \
      * mu ** ( order - r ) \
      * sigma ** r * ir

    irm2 = irm1
    irm1 = ir

  return value

def truncated_normal_ab_pdf ( x, mu, sigma, a, b ):

  if ( x < a ):
  
    value = 0.0
    
  elif ( x <= b ):
  
    alpha = ( a - mu ) / sigma
    beta = ( b - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = normal_01_cdf ( alpha )
    beta_cdf = normal_01_cdf ( beta )
    xi_pdf = normal_01_pdf ( xi )

    value = xi_pdf / ( beta_cdf - alpha_cdf ) / sigma

  else:
  
    value = 0.0
    
  return value

def truncated_normal_ab_pdf_values ( n_data ):

  import numpy as np

  n_max = 11

  a_vec = np.array ( ( \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0 ))

  b_vec = np.array ( ( \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0 ))

  f_vec = np.array ( ( \
    0.01543301171801836, \
    0.01588394472270638, \
    0.01624375997031919, \
    0.01650575046469259, \
    0.01666496869385951, \
    0.01671838200940538, \
    0.01666496869385951, \
    0.01650575046469259, \
    0.01624375997031919, \
    0.01588394472270638, \
    0.01543301171801836 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, a, b, x, f

def truncated_normal_ab_sample ( mu, sigma, a, b ):

  import numpy as np

  alpha = ( a - mu ) / sigma
  beta = ( b - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  u = np.random.rand ( )
  xi_cdf = alpha_cdf + u * ( beta_cdf - alpha_cdf )
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x

def truncated_normal_ab_variance ( mu, sigma, a, b ):

  alpha = ( a - mu ) / sigma
  beta = ( b - mu ) / sigma

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = normal_01_pdf ( beta )

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  value = sigma * sigma * ( 1.0 \
    + ( alpha * alpha_pdf - beta * beta_pdf ) / ( beta_cdf - alpha_cdf ) \
    - ( ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf ) ) ** 2 )

  return value

def truncated_normal_a_cdf_inv ( cdf, mu, sigma, a ):

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'truncated_normal_a_cdf_inv - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'truncated_normal_a_cdf_inv - Fatal error!' )

  alpha = ( a - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = 1.0

  xi_cdf = ( beta_cdf - alpha_cdf ) * cdf + alpha_cdf
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x

def truncated_normal_a_cdf ( x, mu, sigma, a ):

  if ( x < a ):
  
    value = 0.0
    
  else:
  
    alpha = ( a - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = normal_01_cdf ( alpha )
    beta_cdf = 1.0
    xi_cdf = normal_01_cdf ( xi )

    value = ( xi_cdf - alpha_cdf ) / ( beta_cdf - alpha_cdf )

  return value

def truncated_normal_a_cdf_values ( n_data ):

  import numpy as np

  n_max = 11

  a_vec = np.array ( ( \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0 ))

  f_vec = np.array ( ( \
    0.3293202045481688, \
    0.3599223134505957, \
    0.3913175216041539, \
    0.4233210140873113, \
    0.4557365629792204, \
    0.4883601253415709, \
    0.5209836877039214, \
    0.5533992365958304, \
    0.5854027290789878, \
    0.6167979372325460, \
    0.6474000461349729 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, a, x, f

def truncated_normal_a_mean ( mu, sigma, a ):

  alpha = ( a - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = 1.0

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = 0.0

  value = mu + sigma * ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf )

  return value

def truncated_normal_a_moment ( order, mu, sigma, a ):

  value = r8_mop ( order ) \
    * truncated_normal_b_moment ( order, -mu, sigma, -a );

  return value

def truncated_normal_a_pdf ( x, mu, sigma, a ):

  if ( x < a ):
  
    value = 0.0
    
  else:
  
    alpha = ( a - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = normal_01_cdf ( alpha )
    beta_cdf = 1.0
    xi_pdf = normal_01_pdf ( xi )

    value = xi_pdf / ( beta_cdf - alpha_cdf ) / sigma

  return value

def truncated_normal_a_pdf_values ( n_data ):

  import numpy as np

  n_max = 11

  a_vec = np.array ( ( \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0 ))

  f_vec = np.array ( ( \
     0.01507373507401876, \
     0.01551417047139894, \
     0.01586560931024694, \
     0.01612150073158793, \
     0.01627701240029317, \
     0.01632918226724295, \
     0.01627701240029317, \
     0.01612150073158793, \
     0.01586560931024694, \
     0.01551417047139894, \
     0.01507373507401876 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, a, x, f

def truncated_normal_a_sample ( mu, sigma, a ):

  import numpy as np

  alpha = ( a - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = 1.0

  u = np.random.rand ( )
  xi_cdf = alpha_cdf + u * ( beta_cdf - alpha_cdf )
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x

def truncated_normal_a_variance ( mu, sigma, a ):

  alpha = ( a - mu ) / sigma

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = 0.0

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = 1.0

  value = sigma * sigma * ( 1.0 \
    + ( alpha * alpha_pdf - 0.0 ) / ( beta_cdf - alpha_cdf ) \
    - ( ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf ) ) ** 2 )

  return value

def truncated_normal_b_cdf_inv ( cdf, mu, sigma, b ):
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'truncated_normal_b_cdf_inv - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'truncated_normal_b_cdf_inv - Fatal error!' )

  beta = ( b - mu ) / sigma

  alpha_cdf = 0.0
  beta_cdf = normal_01_cdf ( beta )

  xi_cdf = ( beta_cdf - alpha_cdf ) * cdf + alpha_cdf
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x

def truncated_normal_b_cdf ( x, mu, sigma, b ):
  if ( x <= b ):
  
    beta = ( b - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = 0.0
    beta_cdf = normal_01_cdf ( beta )
    xi_cdf = normal_01_cdf ( xi )

    value = ( xi_cdf - alpha_cdf ) / ( beta_cdf - alpha_cdf )

  else:
  
    value = 1.0
    
  return value

def truncated_normal_b_cdf_values ( n_data ):

  import numpy as np

  n_max = 11

  b_vec = np.array ( ( \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0 ))

  f_vec = np.array ( ( \
    0.3525999538650271, \
    0.3832020627674540, \
    0.4145972709210122, \
    0.4466007634041696, \
    0.4790163122960786, \
    0.5116398746584291, \
    0.5442634370207796, \
    0.5766789859126887, \
    0.6086824783958461, \
    0.6400776865494043, \
    0.6706797954518312 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, b, x, f

def truncated_normal_b_mean ( mu, sigma, b ):

  beta = ( b - mu ) / sigma

  alpha_cdf = 0.0
  beta_cdf = normal_01_cdf ( beta )

  alpha_pdf = 0.0
  beta_pdf = normal_01_pdf ( beta )

  value = mu + sigma * ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf )

  return value

def truncated_normal_b_moment ( order, mu, sigma, b ):

  from scipy.special import comb

  if ( order < 0 ):
    print ( '' )
    print ( 'truncated_normal_b_moment - Fatal error!' )
    print ( '  ORDER < 0.' )
    raise Exception ( 'truncated_normal_b_moment - Fatal error!' )

  if ( sigma <= 0.0 ):
    print ( '' )
    print ( 'truncated_normal_b_moment - Fatal error!' )
    print ( '  SIGMA <= 0.0.' )
    raise Exception ( 'truncated_normal_b_moment - Fatal error!' )

  b_h = ( b - mu ) / sigma
  b_pdf = normal_01_pdf ( b_h )
  b_cdf = normal_01_cdf ( b_h )

  if ( b_cdf == 0.0 ):
    print ( '' )
    print ( 'truncated_normal_b_moment - Fatal error!' )
    print ( '  PDF/CDF ratio fails, because B_cdf too small.' )
    print ( '  B_pdf = %g' % ( b_pdf ) )
    print ( '  B_cdf = %g' % ( b_cdf ) )
    raise Exception ( 'truncated_normal_b_moment - Fatal error!' )

  f = b_pdf / b_cdf;

  value = 0.0
  irm2 = 0.0
  irm1 = 0.0

  for r in range ( 0, order + 1 ):

    if ( r == 0 ):
      ir = 1.0
    elif ( r == 1 ):
      ir = - f
    else:
      ir = - b_h ** ( r - 1 ) * f + ( r - 1 ) * irm2

    value = value + comb ( order, r ) \
      * mu ** ( order - r ) \
      * sigma ** r * ir

    irm2 = irm1
    irm1 = ir

  return value

def truncated_normal_b_pdf ( x, mu, sigma, b ):

  if ( x <= b ):
  
    beta = ( b - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = 0.0
    beta_cdf = normal_01_cdf ( beta )
    xi_pdf = normal_01_pdf ( xi )

    value = xi_pdf / ( beta_cdf - alpha_cdf ) / sigma

  else:
  
    value = 0.0
    
  return value

def truncated_normal_b_pdf_values ( n_data ):

  import numpy as np

  n_max = 11

  b_vec = np.array ( ( \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0 ))

  f_vec = np.array ( ( \
    0.01507373507401876, \
    0.01551417047139894, \
    0.01586560931024694, \
    0.01612150073158793, \
    0.01627701240029317, \
    0.01632918226724295, \
    0.01627701240029317, \
    0.01612150073158793, \
    0.01586560931024694, \
    0.01551417047139894, \
    0.01507373507401876 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, b, x, f

def truncated_normal_b_sample ( mu, sigma, b ):

  import numpy as np

  beta = ( b - mu ) / sigma

  alpha_cdf = 0.0
  beta_cdf = normal_01_cdf ( beta )

  u = np.random.rand ( )
  xi_cdf = alpha_cdf + u * ( beta_cdf - alpha_cdf )
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x

def truncated_normal_b_variance ( mu, sigma, b ):

  beta = ( b - mu ) / sigma

  alpha_pdf = 0.0
  beta_pdf = normal_01_pdf ( beta )

  alpha_cdf = 0.0
  beta_cdf = normal_01_cdf ( beta )

  value = sigma * sigma * ( 1.0 \
    + ( 0.0 - beta * beta_pdf ) / ( beta_cdf - alpha_cdf ) \
    - ( ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf ) ) ** 2 )

  return value