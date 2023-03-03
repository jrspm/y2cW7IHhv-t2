
######################################################################################################
################################################ PASO 1 ##############################################
# Crear un entorno de anaconda con los paquetes que considere necesarios.
######################################################################################################

# py -m pip install seaborn  para actulizar paquetes en python CMD, cuando si funciona en anaconda

# si no corre usar power shell para ver los errores

#------------------------------------- inicio paquetes necesarios -------------------------------------

import numpy as np # paquete para arrays

import pandas as pd # paquete para dataframes

import random # se uso este paquete porue se queria que los valores para reducir el porcentaje fuera aleatorio

import seaborn as sns

import matplotlib.pyplot as plt

#------------------------------------- fin paquetes necesarios -------------------------------------

######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################


######################################################################################################
################################################ PASO 2 ##############################################
# Usando sclicing con NumPy separar los datos en 2 datasets: entrenamiento(80 %) y validación
# y pruebas(20 %).
######################################################################################################

#-------------------------------------  inicio data frame cargar datos -------------------------------------

#cargar datos con el nombre del archivo y el numero de columnas, tambien puede reducir en un porcentaje 

class Datos_Proyecto:

    def __init__(self, nombre_archivo,lista_columnas): # todos los atributos del objeto

        self.array_total=np.load(nombre_archivo) #cargar el archivo usando el nombre, debe estar en la carpeta y deber ser un array

        self.lista_columnas_1=lista_columnas #lista del nombre de las columnas de array

        rows, columns = self.array_total.shape #obtener cantidad de filas, columnas del array

        self.cantidad_filas=rows #cantidad de filas del array

        self.array_tolist=self.array_total.tolist() # convertir en lista el array para poder usarlo en pandas

        self.dataframe_total=pd.DataFrame(self.array_tolist, columns=self.lista_columnas_1) # crear el dataframe y nombrar las columnas

        self.data_Reducido_trabajar=self.dataframe_total

        self.data_Reducido_comparar=self.dataframe_total




    def reducir_data(self,porcentaje_reducir): #metodo para reducir el dataframe, porcentaje a reducir

        lista_reducir=[]

        if porcentaje_reducir<1 and porcentaje_reducir>0: # condicionante para reducir

            cantidad_filas_porcentaje=int((self.cantidad_filas)*porcentaje_reducir) #cantidad de filas del porcentaje a reducir


            while len(lista_reducir)<cantidad_filas_porcentaje: # terminar el proceso hasta que se tengan todos los valores de la lista

                valor_random=random.randint(0,self.cantidad_filas-1) # seleccionar un valor random, entre 0 y la cantidad de datos

                if lista_reducir.count(valor_random)==0: # comparar que no exista el valor random
                
                    lista_reducir.append(valor_random) #agregar a la lista el valor random
            
            
            lista_reducir.sort() # ordenar la lista a reducir

            set_range_cantida_filas=set(list(range(self.cantidad_filas-1))) # conjunto de todas las filas dataframe

            lista_reducida_trabajar=list(set_range_cantida_filas.difference(set(lista_reducir))) #diferencia de conjuntos, lista de los valores a trabajar

            self.data_Reducido_trabajar=self.dataframe_total.drop(lista_reducir, axis=0) #dataframe de las filas que se trabajaran

            self.data_Reducido_comparar=self.dataframe_total.drop(lista_reducida_trabajar, axis=0) #dataframe de las filas que se compararan

            return self.data_Reducido_trabajar, self.data_Reducido_comparar

        else:

            print("Valor incorrecto")


    def valor_max_med_min_ptp_desv(self,list_num_int,redondear): #metodo para obtener los valores max_min_medio_ptp_desvi, ingresar 

        dic_val_max_med_min_ptp_desv={"VALORES":("MAXIMO","MEDIA","MINIMO","PEAK TO PEAK","DESVIACION")}

        for i in self.lista_columnas_1:

            data_1=self.data_Reducido_trabajar[i] #DATAFRAME DE CADA COLUMNA i 

            val_max=data_1.max() # obtener el valor maximo del dataframe
            val_med=data_1.mean() # obtener el valor medio del dataframe
            val_min=data_1.min() # obtener el valor minimo del dataframe 
            val_des=data_1.dropna().std() # obtener la desviacion estandar quitando los nan
            val_ptp=np.ptp(data_1.dropna()) # obtener el peak to peak quitando los nan

            val_cancatenados=[val_max,val_med,val_min,val_ptp,val_des] # hacer una lista de los valores

            if list_num_int.count(i)>0: #comparar si una de las columnas esta en el listado de enteros

                val_cancatenados = list(map(int, val_cancatenados)) # redondear enteros cuando la columna lo requiera

            else:

                val_cancatenados =[round(i,redondear) for i in val_cancatenados] # redondear hasta la cifra indicada


            val_cancatenados_1=tuple(val_cancatenados) # convertir en tupla la lista

            dic_val_max_med_min_ptp_desv[i]=val_cancatenados_1 # guardar en el diccionario la tupla con los valores segun la columna

        data_valores = pd.DataFrame(dic_val_max_med_min_ptp_desv) # crear un dataframe apartir de un diccionario
            
        return data_valores #regresa un dataframe con todos los valores

    def histograma_parejas(self,list_graf): #metodo para obtener los valores max_min_medio_ptp_desvi, ingresar 

        for i in list_graf:

            #------- inicio comprobar distribucion --------------------

            #self.data_Reducido_trabajar.sort_values(i[1])

            #data_1=self.data_Reducido_trabajar[i].dropna() #DATAFRAME DE CADA COLUMNA i

            #data_1=data_1.value_counts() #para contar la catidad de valores que hay de un mismo valor 

            #data_1_dic=data_1.to_dict()

            #keys = data_1_dic.keys()
            #sorted_keys = sorted(keys)

            #data_2_dic = {key:data_1_dic[key] for key in sorted_keys}

            #print(data_2_dic)

            #------- fin comprobar distribucion --------------------              

            #------- inicio forma 1 ------------

            #self.data_Reducido_trabajar[i].dropna().hist()

            #plt.show()

            #------- fin forma 1 ------------

            #------- inicio forma 2 ------------

            #data_1=self.data_Reducido_trabajar[i].dropna() #DATAFRAME DE CADA COLUMNA i
       
            #res = pd.Series(data_1,name="Range")

            #plot = sns.distplot(res,rug=False,hist=True)
            
            #plt.show()

            #------- fin forma 2 ------------

            #------- inicio forma 3 ------------

            try:

                data_1=self.data_Reducido_trabajar[i].dropna().values.tolist() #DATAFRAME DE CADA COLUMNA i    

                df = pd.DataFrame(data_1, columns=[i]) # nombrar a la columna 

                plot = sns.displot(data = df, x=i )

                plt.title("")
                plt.xticks(fontsize=9, rotation=45)
                plt.xlabel(i,fontsize=12)
                plt.ylabel('Counted',fontsize=12)
                plt.tight_layout()
                
            except:
                print("ERROR AL GENERAR LA GRAFICA DE LOS HISTOGRAMAS")
                pass

            #------- fin forma 3 ------------

        plt.show()

    def factor_correlacion(self,lista_graf_2,num_parejas):

        list_corr=[]

        cont_1=0

        lista_columns_2=[]

        if num_parejas>len(lista_graf_2):

            print("ERROR EL VALOR DE LAS PAREJAS ES MAYOR A LA CANTIDAD DE LAS LISTAS")

        else:

            try:

                for i in lista_graf_2:

                    cont_1+=1

                    data_1=self.data_Reducido_trabajar[[i[1],i[0]]].dropna()

                    corr_1=data_1.corr().values.tolist()

                    key=i[1]+" VS "+i[0]

                    corr_value=round(corr_1[0][1],4)

                    lista_columns_2.append(key)

                    list_corr.append(corr_value)

                    array_data_1=data_1.values.tolist()

                    array2=np.reshape(array_data_1,-1)

                    lista_x=array2[0:-1:2]

                    lista_y=array2[1::2]          


                    plt.scatter(lista_x,lista_y)
                    plt.title(f"{key} ---- Corr:{corr_value}", fontsize = 12)
                    plt.xticks(fontsize=9, rotation=45)
                    plt.xlabel(i[1],fontsize=12)
                    plt.ylabel(i[0],fontsize=12)
                    plt.tight_layout()
                    plt.show()


                data_valores_corr = pd.DataFrame(list_corr, index=lista_columns_2, columns=["CORRELATIVO"])

                data_valores_corr = data_valores_corr.sort_values('CORRELATIVO',ascending=False)

                data_valores_entre_0_1=data_valores_corr.loc[data_valores_corr["CORRELATIVO"]!= 1, :]

                if (data_valores_entre_0_1.shape[0])>=num_parejas:

                    row_1=data_valores_entre_0_1.head(num_parejas)

                else:
        
                    row_1=data_valores_corr

                return data_valores_corr, row_1

            except: 

                print("Error al generar las graficas de las correlaciones")
                
                pass

    def entrenamiento_80(self,lista_graf_2,epoch,b1,b0,alpha):

        data_1=self.data_Reducido_trabajar[lista_graf_2].dropna()

        num=data_1.shape[0]

        array_list_1=[1]*(num)

        data_1.insert(2, "ones", array_list_1)

        data_2=pd.DataFrame(columns=["b1","b0","error","epoch"])

        def det_error(data_1,lista_graf_2,b1_1,b0_0,alpha_1):

            array_temp_x_1=np.array(data_1[[lista_graf_2[1],"ones"]].values.tolist())

            array_temp_y=np.array(data_1[lista_graf_2[0]].values.tolist())

            array_b1_bo=np.array([b1_1,b0_0])

            array_y_result=np.dot(array_temp_x_1,array_b1_bo)

            data_temp=pd.DataFrame({'x':array_temp_x_1[:, :1].reshape(-1).tolist(),'y_result':array_y_result.tolist(), "y":array_temp_y.tolist()})

            data_temp['(y_result - y)'] = data_temp['y_result'] - data_temp['y']

            data_temp['(y_result - y)^2']=data_temp['(y_result - y)']*data_temp['(y_result - y)']

            data_temp['x(y_result - y)']=data_temp['x']*data_temp['(y_result - y)']

            n_1=float(data_temp.shape[0])

            n_1_2=2

            n_1_2_2=n_1*n_1_2

            sum_1=data_temp['(y_result - y)^2'].sum()
            sum_2=data_temp['x(y_result - y)'].sum()
            sum_3=data_temp['(y_result - y)'].sum()

            div_1=1/n_1_2_2

            error_temp=div_1*sum_1

            b_1_next=b1_1-alpha_1*sum_2/n_1
            b_0_next=b0_0-alpha_1*sum_3/n_1

            return b_1_next, b_0_next, error_temp,b1_1, b0_0

        cont_1=0

        cont_2=0



        while epoch>cont_1:

            if cont_1==0:

                b_1_next, b_0_next, error_temp, b1_1, b0_0=det_error(data_1,lista_graf_2,b1,b0,alpha)

                data_2=data_2.append({"b1":b1_1,"b0":b0_0,"error":error_temp,"epoch":cont_1},ignore_index=True)

            else:

                b_1_next, b_0_next, error_temp, b1_1, b0_0=det_error(data_1,lista_graf_2,b_1_next,b_0_next,alpha)

                if cont_2==3:

                    nuevo_registro = {"b1":b1_1,"b0":b0_0,"error":error_temp,"epoch":cont_1}
 
                    #Añadiendo una fila al dataframe

                    data_2 = data_2.append(nuevo_registro, ignore_index=True)

                    cont_2=0


            cont_1+=1

            cont_2+=1

            


        print(data_2)
               


#-------------------------------------  fin data frame cargar datos -------------------------------------

lista_1=["PRECIO",
    "CALIDAD_MATERIAL",
    "AREA_PISO",
    "TOTAL_HABITACIONES",
    "AÑO_CONSTRUCCION",
    "FRENTE"] # LISTA DE LOS NOMBRES DE LAS COLUMNAS

datos_1=Datos_Proyecto("proyecto_training_data.npy",lista_1) # leer los datos


data_Reducido_from_datos_1=datos_1.reducir_data(0.2) # reducir los datos en el 20%


print(datos_1.dataframe_total) # DATAFRAME DE TODOS LOS DATOS 

print(data_Reducido_from_datos_1[0]) # DATAFRAME  entrenamiento(80 %)

print(data_Reducido_from_datos_1[1]) # DATAFRAME pruebas(20 %)

print("\n")



######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################



######################################################################################################
################################################ PASO 3 ##############################################
# Análisis exploratorio de datos: Para cada variable en el dataset calcular((usando numpy o
# pandas):

# media
# valor máximo
# valor mínimo
# valor rango(peak to peak, no el rango del tensor que por ser vector sabemos que es 1)
# desvianción estándar

######################################################################################################

#------------------------------------- inicio max_min_medio_ptp_desvi -------------------------------------

lista_enteros=["AÑO_CONSTRUCCION"] # columnas que deben ser enteros


#ingresar los valores de la lista de las columnas que deben ser enteros y el valor de los decimales
data_valores=datos_1.valor_max_med_min_ptp_desv(lista_enteros,4) #obtener la media de cada columna en un diccionario

#------------------------------------- fin  max_min_medio_ptp_desvi ------------------------------------------

#print(data_valores)



######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################

######################################################################################################
################################################ PASO 4 ##############################################

#------------------------------------- inicio imprimir histogramas -------------------------------------

#ingresar el listado de las parejas de las columnas que se desean graficar [[y1,x1],[y2,x2]]

lista_of_columns=["PRECIO","CALIDAD_MATERIAL","AREA_PISO","TOTAL_HABITACIONES","AÑO_CONSTRUCCION","FRENTE"]

#datos_1.histograma_parejas(lista_of_columns)

#------------------------------------- fin imprimir histogramas------------------------------------------


######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################

######################################################################################################
################################################ PASO 5 ##############################################

#Para cada variable independiente x :

#1. Calcular el coeficiente de correlación entre x y y.
#2. Graficar x vs y(scatterplot) usando matplotlib.
#3. Colocar el coeficiente de correlación y colocarlo como parte del título de la gráfica.
#4. Basado en la gráfica y el coeficiente de correlación de cada par x,y elegir las 2 variables
#   con más potencial predictivo es decir las 2 variables que presentan mayor correlación
#   entre dicha variable y la variable dependiente.

lista_graf_2=[["PRECIO","PRECIO"],
    ["PRECIO","CALIDAD_MATERIAL"],
    ["PRECIO","AREA_PISO"],
    ["PRECIO","TOTAL_HABITACIONES"],
    ["PRECIO","AÑO_CONSTRUCCION"],
    ["PRECIO","FRENTE"]] 

#ingresa las listas de las tablas que se compararan y se agrega la cantidad de 
#parejas a analizar, quienes serán las mas cercanas a 1, pero no 1 
#data_valores_corr,data_valores_corr_1=datos_1.factor_correlacion(lista_graf_2,2)

#print("TODOS_LOS_VALORES_CORRELATIVOS")
#print(data_valores_corr)
#print()
#print("VALORES_CORRELATIVOS_SELECCIONADOS")
#print(data_valores_corr_1)

######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################

lista_graf_2=["PRECIO","CALIDAD_MATERIAL"]
epoch=100
b1=1
b0=2
alpha=30

data_entrenamiento=datos_1.entrenamiento_80(lista_graf_2,epoch,b1,b0,alpha)


input()


#matrix_1Reducida=dataframe_elemento.drop(lista_surtida, axis=1)

