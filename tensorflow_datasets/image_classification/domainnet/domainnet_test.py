# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""domainnet dataset."""

from tensorflow_datasets.image_classification.domainnet import domainnet
import tensorflow_datasets.public_api as tfds


class DomainnetTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for domainnet dataset."""

  DATASET_CLASS = domainnet.Domainnet
  BUILDER_CONFIG_NAMES_TO_TEST = ['real']
  SPLITS = {
      'train': 2,  # Number of fake train example
      'test': 1,  # Number of fake train example
  }
  DL_DOWNLOAD_RESULT = {'train': 'real_train.txt', 'test': 'real_test.txt'}
  DL_EXTRACT_RESULT = 'img'


if __name__ == '__main__':
  tfds.testing.test_main()
