# -*- coding: utf-8 -*-
"""
This module includes functions to evaluate a NaiveBayesClassifier.
"""

# Author: Jael Zela <jael.ruiz@students.ic.unicamp.br>

from feature_extraction import bigram_feats, feature_extraction
from validation import cross_validation
from datasets import g2crowd


def evaluate_classifier(featxs, datasets):
    posfeats, negfeats = feature_extraction(featxs, datasets)

    print '\ncross validation MLP'
    print cross_validation(posfeats, negfeats, folds=5, classifier='decision_tree')


if __name__ == "__main__":
    evaluate_classifier([bigram_feats], [g2crowd])
