import numpy as np
import matplotlib.pyplot as plt

# ejemplo para randomforest
# en los notebook siempre esta definido train, target y data_keys
# debido a lo anterior, la función se ocupa plot_statistics_all(train, data_keys, n_cv=10, eval_metric=)
def plot_statistics_all(train_set, data_keys, n_cv=10, eval_metric='accuracy'):
    # defino todos los valores que voy a graficar en el eje x
    # para random forest será numero de estimadores -> n_estimators
    n_est = np.arange(5,500,300)
    
    # guardo los accuracy promedio por cada cross validation y su desviación estandar
    scores = {'anger': [], 'fear':[], 'joy':[], 'sadness':[]}
    scores_std = {'anger': [], 'fear':[], 'joy':[], 'sadness':[]}
    
    # se mostrarán 4 graficos, 1 por cada sentimiento, la posición es relativa a una matriz de 2x2
    # de este modo, los datos los necesito tener con esa estructura de 2x2
    keys_iterable = np.array(data_keys).reshape(2,2)
    colors = ['tab:blue','tab:orange','tab:green','tab:red']
    colors_iterable = np.array(colors).reshape(2,2)
    
    # imprimo la metrica que estoy estudiando
    print("metricas: "+ eval_metric)
    
    # por cada sentimiento saco las estadisticas y los guardo en cada dict
    for sentiment in data_keys:
        for n in n_est:
            rfc = get_classifier(n)
            if eval_metric == 'accuracy':
                mean, std, eval_metric = statisticsCV(rfc, train_set[sentiment], n_cv, 'accuracy')
            else: #kappa
                mean, std, eval_metric = statisticsCV(rfc, train_set[sentiment], n_cv, make_scorer(cohen_kappa_score))
            scores[sentiment].append(mean)
            scores_std[sentiment].append(std)
    
    # defino los subplots como 2x2        
    fig, axs = plt.subplots(2, 2, figsize=(15,15))
    
    # seteo cada grafico con sus respectivos datos
    for row in [0,1]:
        for col in [0,1]:
            axs[row, col].plot(n_est, scores[keys_iterable[row][col]], colors_iterable[row][col])
            axs[row, col].plot(n_est, np.array(scores[keys_iterable[row][col]]) + np.array(scores_std[keys_iterable[row][col]]), 'k--')
            axs[row, col].plot(n_est, np.array(scores[keys_iterable[row][col]]) - np.array(scores_std[keys_iterable[row][col]]), 'k--')
            axs[row, col].set_title(keys_iterable[row][col])
    
    # a cada grafico le agrego el nombre a sus ejes y su escala en el eje y
    for ax in axs.flat:
        ax.set(xlabel='cantidad de n_estimators', ylabel=eval_metric)
        ax.set_ylim(0,1)

    plt.show()