class reusable:
    def dropcolums(self,df,columns):
        df=df.drop(*columns)
        return df