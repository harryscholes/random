# PyTables
def saveMatrix(CTK, f):
    with tables.open_file(f, mode='w') as f:
        data = f.create_carray(f.root, 'CTK', atom=tables.Atom.from_dtype(CTK.dtype), shape=CTK.shape, filters=tables.Filters(complevel=9, complib='blosc'))
        data[:] = CTK
    
    
def sliceMatrix(f, ind):
    with tables.open_file(f, mode='r') as f: data = f.root.CTK[ind, :]
    CTK = data[:, ind]
    return CTK
