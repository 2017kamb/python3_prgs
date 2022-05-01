import dask.dataframe as dd
df = dd.read_csv('test.csv', blocksize="16MB")

print('############# start ###########')
print(f"######df#####\n{df}\n######df#####")
print(f"######df.head()#####\n{df.head()}\n######df.head()#####")
print(f"######df.tail()#####\n{df.tail()}\n######df.tail()#####")
print(f"######len(df)#####\nNumber of rows are:  {len(df)}\n######len(df)#####")
print(f"######df.compute()#####\n{df.compute()}\n######df.compute()#####")
print(f"######df.npartitions#####\n{df.npartitions}\n######df.npartitions#####")
print(f"######df.dtypes#####\n{df.dtypes}\n######df.dtypes#####")
print(f"######df.describe()#####\n{df.describe()}\n######df.describe()#####")
print(f"######df.describe().compute()#####\n{df.describe().compute()}\n######df.describe().compute()#####")

print('############# end #############')
