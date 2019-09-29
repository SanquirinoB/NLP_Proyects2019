def statisticsCV(clf, dataset, n_iter=10, eval_metric='accuracy'):
    metrics = cross_val_score(clf, dataset.tweet, dataset.sentiment_intensity, cv= n_iter, scoring=eval_metric)
    mean = np.mean(metrics)
    std = np.std(metrics)
    return mean, std, eval_metric