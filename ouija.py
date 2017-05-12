# Copyright 2017 Francisco Baena
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

import time

import RPi.GPIO as GPIO

class OuijaBoard:
  """Outputs text in binary format through the GPIO ports of RPi.

  Alphabetic characters are displayed in binary format, starting
  from 0 (e.g. A=0, B=1...)

  WARNING: this is a draft, numeric chars + symbols aren't handled 
  properly yet!
  """
  
  def __init__(self,
    channels = [ 5, 6, 13, 19, 26 ]):

    self.channels = channels

    GPIO.setmode(GPIO.BCM)
    for channel in self.channels:
      GPIO.setup(channel, GPIO.OUT)

  def output(self, message):
    """Outputs a string into the ouija board"""

    message += ' '
    for letter in list(message.upper()):
      position = 0
      if letter != ' ':
        position = ord(letter) - 64
      bit_rep = bin(position)[2:]
      bit_rep = '0'*(5-len(bit_rep)) + bit_rep
      self._outputGPIO(bit_rep)
      time.sleep(0.6)
 
  def _outputGPIO(self, bit_rep):
    """Represents the bit representation of a letter through the RPi
    GPIO ports"""

    bit_list = list(bit_rep)
    for i, channel in enumerate(self.channels):
      GPIO.output(channel, 
        GPIO.HIGH if bit_list[i]=='1' else GPIO.LOW)
