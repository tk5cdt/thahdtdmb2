from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import plotly.graph_objects as go
import random
import anvil.server
import time

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.arr = []
    self.btn_CreateArray.enabled = True
    self.arr_merge = [0] * 10

  def ChangeState_button(self, i):
      self.btn_Bubble.enabled = i

  def btn_Bubble_click(self, **event_args):
    n = len(self.arr)
    # Lặp qua tất cả các phần tử trong danh sách
    for i in range(n):
        # Các phần tử cuối cùng đã được đặt đúng vị trí, nên chúng ta có thể bỏ qua chúng
        for j in range(0, n-i-1):
          if self.arr[j] > self.arr[j+1]:
            self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
    self.SortedArray.text = ' '.join(map(str, self.arr))
  pass
  
  def btn_reset_click(self, **event_args):
    self.arr = []
    n = len(self.arr)
    self.ChangeState_button(True)
    self.txt_arr.text = ''
    pass

  def is_integer_sequence(self, input_str):
    # Tách chuỗi thành danh sách các phần tử
    elements = input_str.split(',')
    if len(elements) < 2:
      return False
    # Lặp qua từng phần tử để kiểm tra xem có phải là số nguyên không
    for element in elements:
        element = element.strip()  # Loại bỏ khoảng trắng xung quanh phần tử
        if not element.isdigit():
            return False

    return True
    
  def btn_CreateArray_click(self, **event_args):
    n = len(self.arr)
    for i in range(n):
      self.set_textbox_color(i, self.cyan)
    self.arr = [int(num.strip()) for num in self.txt_arr.text.split(',') if num.strip().isdigit()]
    self.ChangeState_button(True)
    pass

  def txt_arr_change(self, **event_args):
    if self.is_integer_sequence(self.txt_arr.text):
      self.btn_CreateArray.enabled = True
    else:
      self.btn_CreateArray.enabled = False
    pass
