import distribution

def truncated_normal_b_pdf_test ():
  import platform

  print ( '' )
  print ( 'truncated_normal_b_pdf_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  truncated_normal_b_pdf evaluates the PDF' )
  print ( '  of the upper Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean = mu' )
  print ( '    standard deviation = sigma' )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval (-oo,b]' )

  print ( '' )
  print ( '                                                 Stored         Computed' )
  print ( '       X        Mu         S         B             PDF             PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, b, x, pdf1 = truncated_normal_b_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = truncated_normal_b_pdf ( x, mu, sigma, b )

    print ( '  %8.1f  %8.1f  %8.1f  %8.1f  %14g  %14g' \
      % ( x, mu, sigma, b, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'truncated_normal_ab_pdf_test:' )
  print ( '  Normal end of execution.' )
  return

  def truncated_normal_b_cdf_inv_test ( ):
  import platform

  sample_num = 10
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'truncated_normal_b_cdf_inv_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  truncated_normal_b_cdf_inv inverts the CDF of' )
  print ( '  the Truncated Normal distribution.' )

  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval (-oo,%g]' % ( b ) )

  print ( '' )
  print ( '             X            CDF            CDF_inv' )
  print ( '' )

  for i in range ( 0, sample_num ):
    x = truncated_normal_b_sample ( mu, sigma, b )
    cdf = truncated_normal_b_cdf ( x, mu, sigma, b )
    x2 = truncated_normal_b_cdf_inv ( cdf, mu, sigma, b )
    print ( '  %14.6g  %14.6g  %14.6g' % ( x, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'truncated_normal_b_cdf_inv_test' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_mean_test ( ):
  import numpy as np
  import platform

  sample_num = 1000
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'truncated_normal_b_mean_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  truncated_normal_b_mean computes the mean' )
  print ( '  of the Truncated Normal distribution.' )

  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval (-oo,%g]' % ( b ) )

  m = truncated_normal_b_mean ( mu, sigma, b )

  print ( '' )
  print ( '  PDF mean = %g' % ( m ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i] = truncated_normal_b_sample ( mu, sigma, b )

  print ( '' )
  print ( '  Sample size =     %6d' % ( sample_num ) )
  print ( '  Sample mean =     %14g' % ( np.mean ( x ) ) )
  print ( '  Sample maximum =  %14g' % ( np.max ( x ) ) )
  print ( '  Sample minimum =  %14g' % ( np.min ( x ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'truncated_normal_b_mean_test:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_moment_test ( ):

  import numpy as np
  import platform

  test_num = 6
  mu_test =    np.array ( [ 0.0,  0.0,  0.0,   0.0,   0.0,  5.0 ] )
  sigma_test = np.array ( [ 1.0,  1.0,  1.0,   2.0,   2.0,  1.0 ] )
  b_test =     np.array ( [ 0.0, 10.0, -10.0, 10.0, -10.0, 10.0 ] )

  print ( '' )
  print ( 'truncated_normal_b_moment_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  truncated_normal_b_moment evaluates moments' )
  print ( '  of the upper Truncated Normal distribution.' )

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    b = b_test[test]
    print ( '' )
    print ( '  Test = %d, Mu = %g, Sigma = %g, B = %g' \
      % ( test, mu, sigma, b ) )
    print ( ' Order  Moment' )
    print ( '\n' )

    for order in range ( 0, 9 ):
      value = truncated_normal_b_moment ( order, mu, sigma, b )
      print ( '  %2d  %12g' % ( order, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'truncated_normal_b_moment_test:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_pdf_test ( ):

  import platform

  print ( '' )
  print ( 'truncated_normal_b_pdf_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  truncated_normal_b_pdf evaluates the PDF' )
  print ( '  of the upper Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean = mu' )
  print ( '    standard deviation = sigma' )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval (-oo,b]' )

  print ( '' )
  print ( '                                                 Stored         Computed' )
  print ( '       X        Mu         S         B             PDF             PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, b, x, pdf1 = truncated_normal_b_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = truncated_normal_b_pdf ( x, mu, sigma, b )

    print ( '  %8.1f  %8.1f  %8.1f  %8.1f  %14g  %14g' \
      % ( x, mu, sigma, b, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'truncated_normal_ab_pdf_test:' )
  print ( '  Normal end of execution.' )
  return

  def truncated_normal_b_sample_test ( ):

  import platform

  sample_num = 10
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'truncated_normal_b_sample_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  truncated_normal_b_sample samples' )
  print ( '  the upper Truncated Normal distribution.' )

  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval (-oo,%g]' % ( b ) )
  print ( '' )

  print ( '' )
  for i in range ( 0, sample_num ):
    x = truncated_normal_b_sample ( mu, sigma, b )
    print ( '  %4d  %14.6g' % ( i, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'truncated_normal_b_sample_test' )
  print ( '  Normal end of execution.' )
  return

  def truncated_normal_b_variance_test ( ):

  import numpy as np
  import platform

  sample_num = 1000
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'truncated_normal_b_variance_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  truncated_normal_b_variance computes the variance' )
  print ( '  of the Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval (-oo,%g]' % ( b ) )

  value = truncated_normal_b_variance ( mu, sigma, b )

  print ( '' )
  print ( '  PDF variance = %g' % ( value ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i] = truncated_normal_b_sample ( mu, sigma, b )

  value = r8vec_variance ( sample_num, x )

  print ( '' )
  print ( '  Sample size = %d' % ( sample_num ) )
  print ( '  Sample variance = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'truncated_normal_b_variance_test:' )
  print ( '  Normal end of execution.' )
  return