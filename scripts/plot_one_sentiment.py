import numpy as np
import matplotlib.pyplot as plt

# ejemplo para randomforest
# en los notebook siempre esta definido train, target y data_keys
# debido a lo anterior, la función se ocupa:

# for key in train:
#     plot_statistics(train[key], key)

def plot_statistics(dataset, key, n_cv=10, eval_metric='accuracy'):
    n_est = np.arange(100,1100,300)
    scores = list()
    scores_std = list()
    print("metricas: "+eval_metric)
    for n in n_est:
        rfc = get_classifier(n)
        mean, std, eval_metric = statisticsCV(rfc, dataset, n_cv, eval_metric)
        scores.append(mean)
        scores_std.append(std)
        print('sentiment: {} | abscisa: {}, | mean: {} | std: {}  \n'.format(key, n, mean, std))
    plt.figure()
    plt.plot(n_est, scores)
    plt.plot(n_est, np.array(scores) + np.array(scores_std), 'b--')
    plt.plot(n_est, np.array(scores) - np.array(scores_std), 'b--')
    locs, labels = plt.yticks()
    min_value= min(np.subtract(np.array(scores), np.array(scores_std)))
    max_value= max(np.add(np.array(scores), np.array(scores_std)))
    plt.ylim(0,1)
    plt.ylabel(eval_metric)
    plt.xlabel("Parameter: n_estimators ")
    plt.show()