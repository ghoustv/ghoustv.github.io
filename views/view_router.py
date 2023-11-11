from flet import *
import flet as ft

#Containers do SideBar


# views
from assets.views.mobile.HomePage import HomePageMobile
from assets.views.web.HomePageWeb import HomePageWeb







def views_handler_mobile(page):
    
    
    
    #Fontes textuais
    
    page.fonts = {"Pacifico": "/fonts/Pacifico.ttf",
                           "Roboto":"/fonts/Roboto-Regular.ttf",
                           "Josefin":"/fonts/JosefinSans-Regular.ttf",
                           "OpenSans":"/fonts/OpenSans-Regular.ttf",
                           "Playfair":"/fonts/PlayfairDisplay-Regular.ttf",}
    
    
    #Funções de scroll
    
    def go_to_home(e):
        pageview["/"].scroll_to(key="HOME", duration=1000)
    
    def go_to_sobre(e):
        pageview["/"].scroll_to(key="SOBRE", duration=1000)
    
    def go_to_services(e):
        pageview["/"].scroll_to(key="SERVIÇOS", duration=1000)
    def go_to_projects(e):
        pageview["/"].scroll_to(key="PROJETOS", duration=1000)
    def go_to_contact(e):
        pageview["/"].scroll_to(key="CONTATO", duration=1000)
        
        
    def change_tab(e:ft.OnScrollEvent):
        
    
        if e.pixels >=0 and e.pixels <134:
            float_button.opacity = 0
            float_button.update()
        elif e.pixels >=242 and e.pixels <1040:
            float_button.opacity = 1
            float_button.update()
        elif e.pixels >=1045 and e.pixels <2121:
            float_button.opacity = 1
            float_button.update()
        elif e.pixels >=1047 and e.pixels <2321:
            float_button.opacity = 1
            float_button.update()
        elif e.pixels >=3627:
            float_button.opacity = 1
            float_button.update()
        
            
    
    #Componentes separados
        
    Title = ft.ResponsiveRow(
        
        controls=[
            
            ft.Container(
                content=ft.Text(
                    size=15,
        font_family="PlayFair",
        weight="bold",
        color="white",
        spans=[
           
                ft.TextSpan(text="LuminumTechne", on_click=lambda e:go_to_home(e))
                
                ],
            ),
            
            
        
        
            
            
        )]
    )
    
    float_button = ft.FloatingActionButton(bgcolor=ft.colors.WHITE12, on_click=lambda e:go_to_home(e), opacity=0, content=ft.Icon(name=ft.icons.ARROW_UPWARD, color="black"))
    
    tabs_drop = ft.PopupMenuButton(
        content=ft.Container(
            tooltip="Menu de navegação",
            margin=20,
            content=
            ft.Icon(name=ft.icons.MENU_OUTLINED, color="white", ),
            
            ),
        items=[
            
            ft.PopupMenuItem(on_click=lambda e:go_to_home(e),content=ft.Text("HOME", font_family="OpenSans", color="black", weight="bold") ),
            ft.PopupMenuItem(on_click=lambda e:go_to_sobre(e),content=ft.Text("SOBRE", font_family="OpenSans", color="black", weight="bold")),
            ft.PopupMenuItem(on_click=lambda e:go_to_services(e),content=ft.Text("SERVIÇOS", font_family="OpenSans", color="black",weight="bold")),
            ft.PopupMenuItem(on_click=lambda e:go_to_projects(e),content=ft.Text("PROJETOS", font_family="OpenSans", color="black",weight="bold")),
            ft.PopupMenuItem(on_click=lambda e:go_to_contact(e),content=ft.Text("CONTATO", font_family="OpenSans", color="black",weight="bold"))
            
        ]
        
    )
    

    
    #Page view para gerenciar as telas e pages
   
   
    pageview =  {
        '/':View(
            bgcolor="white",
            route="/", 
            padding=0,
            on_scroll=change_tab,
            spacing=0,
            scroll=ft.ScrollMode.ADAPTIVE,
            on_scroll_interval=5,
            controls=[
                ft.AppBar(
                    title=Title,
                    toolbar_height=70,
                    bgcolor="black",
                    actions=[
                    
                        ft.VerticalDivider(color="transparent"),
                        tabs_drop
                    
                    ]),
                HomePageMobile(page),
                float_button
            ]
        ),
    }
    
    return pageview

def views_handler_web(page):
    
    #Fontes textuais
    
    page.fonts = {"Pacifico": "/fonts/Pacifico.ttf",
                           "Roboto":"/fonts/Roboto-Regular.ttf",
                           "Josefin":"/fonts/JosefinSans-Regular.ttf",
                           "OpenSans":"/fonts/OpenSans-Regular.ttf",
                           "Playfair":"/fonts/PlayfairDisplay-Regular.ttf",}
    
    #Funções de scroll
    def go_to_home(e):
        pageview["/"].scroll_to(key="HOME", duration=1000)
        
    def current_tab(e):
        
            index_tab = tab_try.selected_index
            name_tab = tab_try.tabs[index_tab].text
            pageview["/"].scroll_to(key=name_tab, duration=1000)
            
    def change_tab(e:ft.OnScrollEvent):
        
    
        if e.pixels >=0 and e.pixels <334:
            tab_try.selected_index = 0
            float_button.opacity = 0
            float_button.update()
            tab_try.update()
        elif e.pixels >=342 and e.pixels <1040:
            tab_try.selected_index = 1
            float_button.opacity = 1
            float_button.update()
            tab_try.update()
        elif e.pixels >=1045 and e.pixels <2121:
            tab_try.selected_index = 2
            float_button.opacity = 1
            float_button.update()
            tab_try.update()
        elif e.pixels >=1047 and e.pixels <2321:
            tab_try.selected_index = 3
            float_button.opacity = 1
            float_button.update()
            tab_try.update()
        elif e.pixels >=3627:
            tab_try.selected_index = 4
            float_button.opacity = 1
            float_button.update()
            tab_try.update()
        
            
            
            
    
        
        #COMPONENTES
    
    #Componentes separados
        
    Title = ft.Container(
        content=ft.Text(
        font_family="Roboto",
        size=30,
        color="white",
        spans=[
           
                ft.TextSpan(text="LuminumTechne", on_click=lambda e:go_to_home(e))
                
                ],
            ),
        )
    
    float_button = ft.FloatingActionButton(icon=ft.icons.ARROW_UPWARD,bgcolor=ft.colors.WHITE12, on_click=lambda e:go_to_home(e), opacity=0)
    
    tab_try = ft.Tabs(
            divider_color=ft.colors.TRANSPARENT,
            label_color="white",
            indicator_padding = 5,
            indicator_color="white",
            selected_index=0,
            unselected_label_color="white",
            animation_duration=300,
            on_change = current_tab,
            tabs=[
                
                ft.TextButton(text="HOME"),
                ft.TextButton(text="SOBRE"),
                ft.TextButton(text="SERVIÇOS"),
                ft.TextButton(text="PROJETOS"),
                ft.TextButton(text="CONTATO"),
                
                ],
            )
    
    #Page view principal
    
    pageview =  {
        '/':View(
            bgcolor="#f8f4f4",
            route="/", 
            padding=0,
            spacing=0,
            on_scroll=change_tab,
            scroll=ft.ScrollMode.ADAPTIVE,
            on_scroll_interval=5,
            controls=[
                ft.AppBar(
                    leading=ft.VerticalDivider(color="transparent"),
                    title=Title,
                    toolbar_height=70,
                    bgcolor="black",
                    actions=[
                    
                        tab_try,
                        ft.VerticalDivider(color="transparent"),
                    
                    ]),
                HomePageWeb(page),
                float_button
            ]
        ),
    }
    
    return pageview
    

