from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

flags = tf.flags
cfg = flags.FLAGS


# command-line config
flags.DEFINE_string ("data_path",  "data",              "Data path")
flags.DEFINE_string ("save_file",  "models/recent.dat", "Save file")
flags.DEFINE_string ("load_file",  "",                  "File to load model "
                                                        "from")
flags.DEFINE_string ("vocab_file", "data/vocab.pk",     "Vocab pickle file")

flags.DEFINE_integer("batch_size",      32,      "Batch size")
flags.DEFINE_integer("word_emb_size",   352,     "Number of learnable dimensions in "
                                                 "word embeddings")
flags.DEFINE_integer("num_layers",      1,       "Number of RNN layers")
flags.DEFINE_integer("hidden_size",     384,     "RNN hidden state size")
flags.DEFINE_integer("latent_size",     16,      "Latent representation size")
flags.DEFINE_float  ("word_dropout",    0.66,    "Word dropout probability for decoder "
                                                 "input")
flags.DEFINE_integer("softmax_samples", 1000,    "Number of classes to sample for "
                                                 "softmax")
flags.DEFINE_float  ("max_grad_norm",   20.0,    "Gradient clipping")
flags.DEFINE_integer("anneal_bias",     3500,    "The step to reach 0.5 for KL "
                                                 "divergence weight annealing")
flags.DEFINE_bool   ("training",        True,    "Training mode, turn off for testing")
flags.DEFINE_string ("optimizer",       "adam",  "Optimizer to use (sgd, adam, adagrad, "
                                                 "adadelta)")
flags.DEFINE_float  ("learning_rate",   1e-3,    "Optimizer initial learning rate")
flags.DEFINE_integer("max_epoch",       10000,   "Maximum number of epochs to run for")
flags.DEFINE_integer("max_steps",       9999999, "Maximum number of steps to run for")

flags.DEFINE_integer("print_every",     50,      "Print every these many steps")
flags.DEFINE_integer("save_every",      -1,      "Save every these many steps (0 to "
                                                 "disable, -1 for each epoch)")
flags.DEFINE_bool   ("save_overwrite",  True,    "Overwrite the same file each time")
flags.DEFINE_integer("validate_every",  1,       "Validate every these many epochs (0 "
                                                 "to disable)")
