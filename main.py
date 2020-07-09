import numpy as np
import Feedforward
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.list import OneLineListItem, OneLineIconListItem
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel

from kivymd.app import MDApp

# Window.size = (600,500)


KV = '''

<Item>

    ImageLeftWidget:
        source: root.source

<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "wheat.png"

    MDLabel:
        text: "Crop Predictor"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "Contact Info - ragib.hussain70@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        MDList:

            OneLineAvatarListItem:
                text: "USA Predictor"

                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

                ImageLeftWidget:
                    source: "USA_flag_icon.png"

            OneLineAvatarListItem:
                text: "USA Crops"

                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"

                ImageLeftWidget:
                    source: "USA_flag_icon.png"


Screen:



    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"

                MDToolbar:
                    id: toolbar
                    pos_hint: {"top": 1}
                    elevation: 10
                    title: "USA Crop Predictor"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                MDGridLayout:
                    cols: 1
                    padding: "30dp"
                    spacing: "10dp"

                    MDBoxLayout:

                    MDTextField:
                        id: nitrogen
                        hint_text: "Nitrogen Content"
                        max_text_length: 6
                        icon_right: "percent"
                        mode: "rectangle"
                        #pos_hint: {'center_x' : 0.5, 'center_y': 1 }
                        helper_text: "Enter content in % upto 5 decimal places"
                        helper_text_mode: "on_focus"
                        halign: "center"

                    MDTextField:
                        id: phosphorus
                        hint_text: "Phosphorus Content"
                        max_text_length: 6
                        icon_right: "percent"
                        mode: "rectangle"
                        # pos_hint: {'center_x' : 0.5, 'center_y': 0.5 }
                        helper_text: "Enter content in % upto 5 decimal places"
                        helper_text_mode: "on_focus"
                        halign: "center"

                    MDTextField:
                        id: potassium
                        hint_text: "Potassium Content"
                        max_text_length: 6
                        icon_right: "percent"
                        mode: "rectangle"
                        # pos_hint: {'center_x' : 0.5, 'center_y': 0.5 }
                        helper_text: "Enter content in % upto 5 decimal places"
                        helper_text_mode: "on_focus"
                        halign: "center"

                    MDTextField:
                        id: moisture
                        hint_text: "Moisture Content"
                        max_text_length: 6
                        mode: "rectangle"
                        icon_right: "percent"
                        # pos_hint: {'center_x' : 0.5, 'center_y': 0.5 }
                        helper_text: "Enter content in % upto 5 decimal places"
                        helper_text_mode: "on_focus"
                        halign: "center"

                    MDGridLayout:
                        cols: 2
                        spacing: "50dp"
                        padding: "30dp"

                        MDRectangleFlatButton:
                            text: "Suggest"
                            size_hint: (0.2,None)
                            height: dp(50)
                            on_release:
                                app.predict()

                        MDRectangleFlatButton:
                            text: "Reset"
                            size_hint: (0.2,None)
                            height: dp(50)
                            on_release:
                                app.reset()


            Screen:
                name: "scr 2"

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "USA Crops"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                    ScrollView:

                        MDList:
                            id: md_list
                            #
                            # MDCard:
                            #     size_hint: None, None
                            #     size: root.width,300
                            #     pos_hint: {"center_x": .5, "center_y": .5}
                            #     Image:
                            #         source:"USA_flag_icon.png"
                            #         allow_stretch:"True"
                            #         keep_ratio:"False"
                            #
                            # MDCard:
                            #     size_hint: None, None
                            #     size: self.parent.width,300
                            #     pos_hint: {"center_x": .5, "center_y": .5}


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()


class TestNavigationDrawer(MDApp):

    def close_dialog(self,obj):
        self.dialog.dismiss()


    def reset(self):
        self.root.ids.moisture.text = ""
        self.root.ids.nitrogen.text = ""
        self.root.ids.potassium.text = ""
        self.root.ids.phosphorus.text = ""


    def predict(self):
        if(self.root.ids.moisture.text=="" or self.root.ids.nitrogen.text=="" or self.root.ids.phosphorus.text=="" or self.root.ids.potassium.text==""):
            alert1 = "Insufficient Data"
            close_button1 = MDFlatButton(text="Dismiss", on_release= self.close_dialog)
            self.dialog = MDDialog(
                    title="Warning",
                    text=alert1,
                    radius=[20, 7, 20, 7],
                    size_hint= (0.75,0.8),
                    buttons= [close_button1])
            self.dialog.open()
            return

        num1 = np.asfarray(self.root.ids.moisture.text, float)
        num2 = np.asfarray(self.root.ids.nitrogen.text, float)
        num3 = np.asfarray(self.root.ids.phosphorus.text, float)
        num4 = np.asfarray(self.root.ids.potassium.text, float)
        result = Feedforward.output_results(num1, num2, num3, num4)
# Display the result
        close_button2 = MDFlatButton(text="Dismiss", on_release= self.close_dialog)
        self.dialog = MDDialog(
                title="Crop Suggestions",
                type="simple",
                items=[
                    Item(text=result[0],source="wheat.png"),
                    Item(text=result[1],source="wheat.png"),
                    Item(text=result[2],source="wheat.png"),
                    Item(text=result[3],source="wheat.png"),
                    Item(text=result[4],source="wheat.png")],
                radius=[20, 7, 20, 7],
                size_hint= (0.75,0.8),
                buttons= [close_button2])
        self.dialog.open()


    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def on_start(self):
        for crop in sorted(Feedforward.labels):
            card = MDCard(orientation='vertical',size_hint=(None,None), size = (self.root.width,300))
            imgr = Image(source="images/"+str(crop)+str(".jpg"), size_hint_y = 0.8, allow_stretch="True", keep_ratio="False")
            lbl = MDLabel(text=str(crop), size_hint_y = 0.2, halign = 'center', valign = 'center')
            card.add_widget(imgr)
            card.add_widget(lbl)
            self.root.ids.md_list.add_widget(card)



TestNavigationDrawer().run()
