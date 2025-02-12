import numpy as np 

data_folder = '../Data/Dataset/'
field_folder = '../Data/Fields/'

#File functions
def Load_file(filename):
    File_data = np.loadtxt(filename, dtype=np.float32)
    return File_data

def Save_file(data, filename):
    np.savetxt(filename, data)

def Save_file_3D(data,filename):
    np.save(filename,data,allow_pickle=True) 

def Load_file_3D(filename):
    filename1 = filename+".npy"
    dat = np.load(filename1,allow_pickle=True)
    return dat

def open_file_fmhd(filename):
	with open(filename, 'rb') as f:	
		dt = np.dtype((np.float32,1))
		d1=np.fromfile(f, dtype=dt)

	ny = int(d1[0])
	nz = int(d1[1])
	nx = int(d1[2])

	with open(filename, 'rb') as f:	
		f.seek(24)
		dt = np.dtype((np.float32,(nx,nz,ny)))
		data=np.fromfile(f, dtype=dt)
		
	bx = data[0,:,:,:]
	by = data[1,:,:,:]
	bz = data[2,:,:,:]

	bx1=np.transpose(bx,[0,2,1])
	by1=np.transpose(by,[0,2,1])
	bz1=np.transpose(bz,[0,2,1])

	Save_file_3D(bx1, field_folder + "Field in x")
	Save_file_3D(by1, field_folder + "Field in y")
	Save_file_3D(bz1, field_folder + "Field in z")
        
def open_file_pluto():
	t=0
	xpt=256
	ypt=256
	zpt=256

	filename = 'Pluto/Bx1.'+ str(t).zfill(4)+'.dbl'
	print(data_folder+filename)
	shape=(zpt,ypt,xpt)
	fd = open(filename, 'rb')
	data = np.fromfile(file=fd, dtype=np.float64).reshape(shape)
	bx=data.transpose()

	filename='Pluto/Bx2.'+str(t).zfill(4)+'.dbl'
	print(data_folder+filename)
	shape=(zpt,ypt,xpt)
	fd = open(filename, 'rb')
	data = np.fromfile(file=fd, dtype=np.float64).reshape(shape)
	by=data.transpose()

	filename='Pluto/Bx3.'+str(t).zfill(4)+'.dbl'
	print(data_folder+filename)
	shape=(zpt,ypt,xpt)
	fd = open(filename, 'rb')
	data = np.fromfile(file=fd, dtype=np.float64).reshape(shape)
	bz=data.transpose()

	print(bx[10,20,30],by[10,20,30],bz[10,20,30])

	Save_file_3D(bx, field_folder + "Field in x")
	Save_file_3D(by, field_folder + "Field in y")
	Save_file_3D(bz, field_folder + "Field in z")

