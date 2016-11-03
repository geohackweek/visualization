
def read_asc_file(file_path, verbose=True):
    import numpy as np
    asc_file = open(file_path, 'r')
    
    tokens = asc_file.readline().split()
    ncols = int(tokens[1])
    
    tokens = asc_file.readline().split()
    nrows = int(tokens[1])
    
    tokens = asc_file.readline().split()
    xllcorner = float(tokens[1])
    
    tokens = asc_file.readline().split()
    yllcorner = float(tokens[1])
    
    tokens = asc_file.readline().split()
    cellsize = float(tokens[1])
    
    tokens = asc_file.readline().split()
    nodata_value = float(tokens[1])
    
    if verbose:
        print "ncols = %i" % ncols
        print "nrows = %i" % nrows
        print "xllcorner = %g" % xllcorner
        print "yllcorner = %g" % yllcorner
        print "cellsize = %g" % cellsize
        print "nodata_value = %g" % nodata_value
        
    # read in all the data, assumed to be on ncols lines, 
    # each containing nrows values
    
    asc_file.close()  # close file so we can load array
    asc_data = np.loadtxt(file_path, skiprows=6)  # skip header
    
    # reshape
    values = asc_data.reshape((nrows,ncols))
    
    # flip in y because of data order
    values = np.flipud(values)    
    
    x = xllcorner + cellsize * np.arange(0,ncols)
    y = yllcorner + cellsize * np.arange(0,nrows)
    
    X,Y = np.meshgrid(x,y)
        
    asc_data_dict = {'ncols': ncols, 'nrows': nrows, 'xllcorner':xllcorner, \
                     'yllcorner':yllcorner, 'cellsize':cellsize, \
                     'nodata_value':nodata_value, \
                     'X': X, 'Y':Y, 'values': values}
    return asc_data_dict


