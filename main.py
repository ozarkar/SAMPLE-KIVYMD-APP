
from kivy.lang.builder import Builder
from kivymd.app import MDApp
# from kivy.core.window import Window
# Window.size=(350,600)

KV = '''
MDFloatLayout:
  MDLabel:
    text: 'Login Form'
    pos_hint:{'center_y':.85}
    font_size: '30sp'
    halign:'center'
    bold:True
    theme_text_color:'Custom'
    text_color:'red'

  MDLabel:
    text:'Welcome To TaTa'
    pos_hint:{'center_y':.80}
    font_size: '15sp'
    halign:'center'
    bold:True
    theme_text_color:'Custom'
    text_color:0,0,0,1 

  MDTextField:
    id:fname
    hint_text:'Enter First Name'
    pos_hint:{'center_x':.5, 'center_y':.6}
    current_hint_text_color:0,0,0,1
    size_hint_x:.6

  MDTextField:
    id:lname
    hint_text:'Enter Last Name'
    pos_hint:{'center_x':.5, 'center_y':.5}
    current_hint_text_color:0,0,0,1
    size_hint_x:.6

  MDTextField:
    id:output
    hint_text:'output'
    pos_hint:{'center_x':.5, 'center_y':.4}
    current_hint_text_color:0,0,0,1
    size_hint_x:.6
 

  MDRaisedButton:
    id:submit
    text:'Submit'
    pos_hint:{'center_x':.5, 'center_y':.25}
    size_hint_x:.5
    bold:True
    on_press:app.submit(fname.text, lname.text)


  




'''


class ProjectApp(MDApp):
      
  def build(self):
    kv = Builder.load_string(KV)
    return kv

  def submit(self, fname, lname):
    a = int(fname)+int(lname)
    self.root.ids.output.text=f'{a}'
    
if __name__ in ('__main__', '__android__'):
  ProjectApp().run()
