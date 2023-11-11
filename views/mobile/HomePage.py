import flet as ft
import smtplib
from email.mime.text import MIMEText
import time

class HomePageMobile(ft.UserControl):

    def __init__(self,page):
            super().__init__()
            self.page = page
            
    def build(self):
        
        
        field_empty = ft.AlertDialog(
        content=ft.ResponsiveRow(
            spacing=10,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,controls=[ft.Icon(name=ft.icons.CANCEL_OUTLINED,size=25, color="red"),ft.Text("Será necessário preencher todos os dados para envio!" ,weight="bold",color="black",font_family="OpenSans" ,)])
    )
        mail_sucess_dialog = ft.AlertDialog(
        
        content=ft.ResponsiveRow(spacing=10,alignment=ft.MainAxisAlignment.SPACE_BETWEEN,controls=[ft.Icon(name=ft.icons.CHECK_CIRCLE_OUTLINE,size=25, color="green"),ft.Text("E-mail enviado com sucesso!", weight="bold",color="black",font_family="OpenSans" ,)])
    
    )
        
        erro_conexion_dialog = ft.AlertDialog(
        
        content=ft.ResponsiveRow(spacing=10,alignment=ft.MainAxisAlignment.SPACE_BETWEEN,controls=[ft.Icon(name=ft.icons.SIGNAL_WIFI_CONNECTED_NO_INTERNET_4_SHARP,size=25, color="red"),ft.Text("Erro na conexão!, verifique sua rede.", font_family="OpenSans" ,weight="bold",color="black")])
    
    )
        Carregar_dialog = ft.AlertDialog(
        
        title=ft.Text("Carregando envio..."),
        content = ft.ProgressRing(width=16, height=36)
    )


      
            
        #VARIAVEIS
        
        
        mail_name = ft.TextField(label="Seu Nome",  color="black")
        mail_address = ft.TextField(label="Seu Email",  color="black")
        mail_subject = ft.TextField(label="Assunto",color="black")
        mail_message = ft.TextField(label="Mensagem", multiline=True, color="black", max_lines=5)
        
        def enviar_email(e):
            
            def carregar_envio(e):
                self.page.dialog = Carregar_dialog
                Carregar_dialog.open = True
                self.page.update()
                
           
            def email_success(e):
                mail_sucess_dialog.opacity = 1
                self.page.dialog = mail_sucess_dialog
                mail_sucess_dialog.open = True
                self.page.update()
                
        
            def open_dialog_empty_field(e):
                self.page.dialog = field_empty
                field_empty.open = True
                self.page.update()
                
            def erro_conexion(e):
                self.page.dialog = erro_conexion_dialog
                erro_conexion_dialog.open = True
                self.page.update()
            
           
                
            
            #TRATATIVA DO EMAIL
            
            try: 
                
                
            
                
            
                if mail_name.value != "" and mail_address.value !="" and mail_message.value !="" and mail_subject.value !="":
                    carregar_envio(e)
                    
                    key = "zcmh nuui gnat uazr"
                    
                    
                    
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.login("gustavocoopoliver@gmail.com", key)
                    server.sendmail(
                    mail_address.value,
                    "gustavocoopoliver@gmail.com",
                    msg=f"""
                    Nome: {mail_name.value}
                    E-mail de envio: {mail_address.value}
                    Assunto: {mail_subject.value}
                    
                    Mensagem: {mail_message.value}
                    """
                    )
                    
                    
                    
                    
                    server.quit()
                    
                    mail_address.value = ""
                    mail_address.update()
                    mail_message.value = ""
                    mail_message.update()
                    mail_name.value = ""
                    mail_name.update()
                    mail_subject.value = ""
                    mail_subject.update()
                    self.page.close_dialog()
                    time.sleep(0.5)
                    email_success(e)
                    
                    
                    
                    
                
                else:
                    self.page.close_dialog()
                    time.sleep(0.5)
                    open_dialog_empty_field(e= None)
                    
            except Exception as ex:
                self.page.close_dialog()
                time.sleep(0.5)
                print(ex)
                erro_conexion(e=None)
                
     
        #Dicionário para Serviços
        
        Servicos = {
            "Desenvolvedor Web": {"icon":"WEB",
                                  "title":"DESENVOLVIMENTO WEB",
                                  "text":"Realizado desenvolvimento web com flet(flutter para python), Django e Flask dependendo do desejo do cliente usando a parte front-end HTML, CSS ou Flutter",},
            "Desenvolvedor Mobile":{"icon":"PHONE_ANDROID",
                                    "title":"DESENVOLVIMENTO MOBILE",
                                  "text":"Criação de sistemas mobile com Progressive Web Aplication. É usado também Frameworks em Python para criação de aplicativos nativos como BEEWARE ",},
            "Desenvolvedor Desktop":{"icon":"DESKTOP_WINDOWS",
                                     "title":"DESENVOLVIMENTO DESKTOP",
                                  "text":"Criação de Aplicações Desktop com Frameworks em python com todo back-end feito em Python",},
            "ChatBots":{"icon":"CHAT",
                        "title":"CHATBOTS",
                                  "text":"Criação e uso de APIs para criação de ChatBots para atendimento comercial automatizado",},
            "PWA":{"icon":"APPS",
                   "title":"PROGRESSIVE WEB APPLICATION",
                                  "text":"Criação de aplicativo responsivo e adaptável para todas as plataformas e instalável.",},
            }
        
        #Dicionário de Projetos
        
        Projetos = {"Portifolio":{"title":"LUMINUSTECHNE",
                                  "image":"/projetos/PORTIFOLIO.jpeg",
                                  "text":"Portifólio sobre meus serviços e projetos.",
                                  "type":"Web/pwa",
                                  "data":"30/10/2023"},
                    "RobotTrade":{"title":"Xripto",
                                  "image":"/projetos/XRIPTOR.jpeg",
                                  "text":"Robô para realizar automaticamente a venda e compra de criptomoedas com base em estratégias e notificar pelo Telegram.",
                                  "type":"Mobile",
                                  "data":"02/02/2023"},
                    "SIGOA":{"title":"Sistema de Gerenciamento ",
                                  "image":"/projetos/SIGOA.jpeg",
                                  "text":"É um sistema desktop para gerenciamento de produtos, logística, vendas, perfis",
                                  "type":"Desktop",
                                  "data":"26/04/2022"},
                    "SOON":{"title":"EM BREVE",
                                  "image":"None",
                                  "text":"Está em processo de construção um E-comerce no nicho de moda",
                                  "type":"E-Comerce",
                                  "data":""},
                                }
        
        #Descrição sobre mim
        
        sobre_mim = """
        Me chamo Gustavo Oliveira e sou desenvolvedor de soluções digitais. Formado pela universidade Estácio de Sá em análise e desenvolvimento de sistemas desde 2022, e Formado em pós de ciência de dados e pós de Inteligência Artificial, busco com proatividade desenvolver sistemas e tecnologias que solucionam algum dilema do cotidiano. Tenho ao todo 5 anos de experiência com desenvolvimento e principalmente com a linguagem Python 
        
        Já desenvolvi para diversos nichos com a linguagem Python, automatizando processos, criando scripts para área de segurança tecnologica, desenvolvendo aplicativos mobile, sistemas desktop e web e trabalho com uma ferramenta BPM, que se chama PEGA.
        
        Hoje tenho projetos como chatbots financeiros que fazem transações de criptomoedas e notificam através da API do Telegram. 
        
        Meu hobby é estudar constantemente inovações para melhorar o dia a dia como inteligências capazes de realizarem trabalhos manuais repetitivos caseiros como robôs limpadores entre outros. """
        
        #Sections SOBRE MIM

        Section_top_body = ft.Container(
            width=self.page.width,
            bgcolor='#f8f4f4',
            padding=ft.padding.only(top=30),
            content=ft.ResponsiveRow(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    
                    ft.Container(bgcolor="white",
                                key="SOBRE",
                                col={"xs":10,"sm": 15, "md": 10, "xl": 10},
                                border_radius=ft.border_radius.all(15),
                                shadow=ft.BoxShadow(
                                                        spread_radius=1,
                                                        blur_radius=15,
                                                        color=ft.colors.BLACK,
                                                        offset=ft.Offset(0, 0),
                                                        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                                width=self.page.width/1.25,
                                
                                content=ft.Column(
                                    controls=[
                                        
                                        ft.Container(
                                                    height=600,
                                                    padding=0,
                                                    margin=0,
                                                    width=self.page.width/1.25,
                                                    content = ft.Column(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        
                                                        controls=[
                                                            
                                                            ft.Container(
                                                                padding=ft.padding.all(0),
                                                                content=ft.Row(
                                                                    controls=[
                                                                        
                                                                        ft.Container(
                                                                            width=200,
                                                                            height=200,
                                                                            content=ft.Image(src="/3x4.jpeg")
                                                                            
                                                                            
                                                                        ),
                                                                        
                                                                    ]
                                                                    
                                                                )
                                                                
                                                            ),
                                                            
                                                            ft.Container(
                                                                height=400,
                                                                padding=ft.padding.only(left=10),
                                                                width=550,
                                                                content=ft.Column(
                                                                    controls=[
                                                                        
                                                                        
                                                                        
                                                                        ft.Container(
                                                                            padding=ft.padding.only(top=20),
                                                                            content=ft.Column(
                                                                            controls=[
                                                                                
                                                                                ft.Row(controls=[ft.Text(weight="bold", size=28, text_align="left", value="Skills", font_family="PlayFair")]),
                                                                                ft.Divider(color="transparent"),
                                                                                
                                                                                ft.ResponsiveRow(
                                                                            controls=[
                                                                                
                                                                                ft.Text("Python: 85%", font_family="Roboto", size=20, weight="bold" , color="black"),
                                                                                
                                                                                
                                                                            ]
                                                                        ),
                                                                                ft.ResponsiveRow(
                                                                            alignment="center"        ,
                                                                            controls=[
                                                                                
                                                                                ft.ProgressBar(value=0.8, bgcolor="#eeeeee", width=400, bar_height=20, tooltip="85%"),
                                                                                
                                                                                
                                                                            ]
                                                                        ),
                                                                                
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                
                                                                                    ft.Text("Html/CSS: 70%", font_family="Roboto", size=20, weight="bold", color="black")
                                                                            ]
                                                                        ),
                                                                                
                                                                                ft.ResponsiveRow(
                                                                            controls=[
                                                                                
                                                                                ft.ProgressBar(value=0.7, bgcolor="#eeeeee", width=400, bar_height=20, tooltip="70%"),
                                                                                
                                                                                
                                                                            ]
                                                                        ),
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                
                                                                                    ft.Text("SQL: 65%", font_family="Roboto", size=20, weight="bold", color="black")
                                                                            ]
                                                                        ),
                                                                                
                                                                                ft.ResponsiveRow(
                                                                            controls=[
                                                                                
                                                                                ft.ProgressBar(value=0.65, bgcolor="#eeeeee", width=400, bar_height=20, tooltip="65%"),
                                                                                
                                                                                
                                                                            ]
                                                                        ),
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                        
                                                                                    ft.Text("PEGA: 60%", font_family="Roboto", size=20, weight="bold", color="black")
                                                                            ]
                                                                        ),
                                                                                
                                                                                ft.ResponsiveRow(
                                                                            controls=[
                                                                                
                                                                                ft.ProgressBar(value=0.6, bgcolor="#eeeeee", width=400, bar_height=20, tooltip="60%"),
                                                                                
                                                                                
                                                                            ]
                                                                        ),
                                                                                
                                                                            ]
                                                                        ),
                                                                        ),
                                                                        
                                                                        
                                                                        
                                                                        
                                                                    ]
                                                                )
                                                            )
                                                        

                                                        
                                                        ]
                                                        
                                                        )),           
                                        
                                        ft.Container(
                                                    height=600,
                                                    width=self.page.width/1.25,
                                                    content=ft.Column(
                                                        scroll=ft.ScrollMode.ADAPTIVE,
                                                        controls=[
                                                            ft.Divider(color="transparent"),
                                                           
                                                            ft.Container(
                                                                padding=ft.padding.only(left=20),
                                                                content=ft.Row(
                                                                    
                                                                    controls=[
                                                                        
                                                                        ft.Container(
                                                                            padding=ft.padding.all(0),
                                                                            border= ft.border.only(bottom=ft.border.BorderSide(4, "blue")),
                                                                            content=ft.Text("Sobre mim", size=30, font_family="PlayFair", color="black"),
                                                                        )
                                                                        
                                                                        
                                                                    ]
                                                                    
                                                                )
                                                            ),
                                                            
                                                             ft.Container(
                                                                 
                                                                padding=ft.padding.only(left=20, right=10, bottom=10),
                                                                content=ft.ResponsiveRow(
                                                                    
                                                                    controls=[
                                                                        
                                                                        ft.Text(value=sobre_mim, font_family="PlayFair",size=15, text_align=ft.TextAlign.START, color="black"),
                                                                        
                                                                        
                                                                    ]
                                                                    
                                                                )
                                                            ),
                                                             
                                                              
                                                            
                                                            
                                                            
                                                            ]
                                                        
                                                    )
                                                    ),
                                    ]
                                     
                                 ))
                    
                ]
                
            )
        )

        #Sections Serviço
        
        Section_body_Service = ft.Container(
            key="SERVIÇOS",
            width=self.page.width,
            alignment=ft.alignment.center,
            bgcolor="#f8f4f4",
            content=ft.ResponsiveRow(
                    alignment=ft.MainAxisAlignment.CENTER,
                    key="row_services", 
                    controls=[
                                    
                                        
                                         
                                    ]
                                     
                                )
                            )
        
        #Sections Projetos
        
        Section_body_projects = ft.Container(
            key="PROJETOS",
            width=self.page.width,
            alignment=ft.alignment.center,
            bgcolor="#f8f4f4",
            content=ft.ResponsiveRow(
                controls=[
                    
                    
                ]
                
            )
        )
        
        #Sections de Contato
        
        Section_body_contact = ft.Container(
            width=self.page.width,
            padding=ft.padding.only(bottom=30, top=30),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.Alignment(0.8, 1),
                colors=["#020024", "#090979", "#00d4ff"],
            ),
            alignment=ft.alignment.center,
            content=ft.ResponsiveRow(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    
                    ft.Container(bgcolor="white",
                                key="CONTATO",
                                col={"xs":10,"sm": 15, "md": 10, "xl": 10},
                                width=self.page.width/1.25,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        
                                        ft.Container(
                                                    padding=10,
                                                    height=600,
                                                    width=self.page.width/1.25,
                                                    content = ft.Column(
                                                        spacing=10,
                                                        controls=[
                                                          
                                                          ft.ResponsiveRow(
                                                              spacing=30,
                                                              controls=[
                                                                  
                                                                  
                                                                  ft.Divider(color="transparent"),
                                                                  ft.Container(content=ft.Text("Me envie um E-mail" ,size=25, weight="bold", color="black"),border= ft.border.only(bottom=ft.border.BorderSide(4, "blue")),),
                                                                  ft.Divider(color="transparent"),
                                                                  ft.Divider(color="transparent"),
                                                              ]
                                                              
                                                              ),
                                                          
                                                          ft.ResponsiveRow(
                                                              controls=[mail_name]
                                                              
                                                              ),
                                                          ft.ResponsiveRow(
                                                              controls=[mail_address]
                                                              
                                                              ),
                                                          ft.ResponsiveRow(
                                                              controls=[mail_subject]
                                                              
                                                              ),
                                                          ft.ResponsiveRow(
                                                              controls=[mail_message]
                                                              
                                                              ),
                                                          ft.Row(
                                                              alignment=ft.MainAxisAlignment.CENTER,
                                                              controls=[ft.FilledButton(text="Enviar", height=50, width=150, on_click=lambda e: enviar_email(e))]
                                                              
                                                              ),
                                                          
                                                            
                                                        ]
                                                    )
                                        ),
                                        
                                        ft.Container(
                                                height=700, 
                                                padding=10,
                                                alignment=ft.alignment.center,
                                                width=self.page.width/1.25,
                                                margin=0,
                                                content = ft.Column(
                                                    spacing=10,
                                                    controls=[
                                                        ft.Divider(color="transparent"),
                                                        ft.ResponsiveRow(
                                                            controls=[
                                                                
                                                                ft.Container(
                                                                    
                                                                    border= ft.border.only(bottom=ft.border.BorderSide(4, "blue")),
                                                                    content=ft.Text("Entre em Contato" ,size=25, weight="bold", color="black")
                                                            
                                                        )
                                                                ]
                                                        
                                                            
                                                            ),
                                                        ft.Divider(color="transparent"),
                                                        ft.ResponsiveRow(
                                                        
                                                            controls=[ft.Text("Quero agradecer por você ter chegado até aqui demonstrando que visualizou todo meu portifólio, sinta-se a vontade para me contactar pelas redes sociais abaixo, pois seu contato será muito importante para minha carreira.",text_align="justify",font_family="OpenSans" ,color="black", size=19)]
                                                            
                                                            ),
                                                        ft.Divider(color="transparent"),
                                                        
                                                        
                                                        
                                                        
                                                        ft.Row(
                                                            controls=[ft.IconButton(icon=ft.icons.PHONE_ANDROID_OUTLINED, icon_color="blue", icon_size=18, disabled=True),
                                                                ft.ResponsiveRow(controls=[ft.Text(spans=[ft.TextSpan(text="+55(21)98560-8605",style=ft.TextStyle(size=17, color="black"),url="https://api.whatsapp.com/send?phone=5521985608605")])]),
                                                                ]
                                                            
                                                            ),
                                                        ft.Row(
                                                            controls=[ft.IconButton(icon=ft.icons.MAIL, icon_color="blue", icon_size=18, disabled=True),
                                                                ft.ResponsiveRow(controls=[ft.Text(spans=[ft.TextSpan(text="gustavocoopoliver@gmail.com",style=ft.TextStyle(size=17, color="black"),url="mailto:gustavocoopoliver@gmail.com?subject=Contato%20com%20desenvolvedor&body=Prezado!%0A%0AGostaria%20de%20saber%20mais%20sobre%20voc%C3%AA!%0A%0AAtenciosamente.")])]),
                                                                ]
                                                            
                                                            ),
                                                        ft.Divider(color="transparent"),
                                                        ft.Row(
                                                            controls=[
                                                                ft.IconButton(tooltip="Facebook" ,icon_color="blue",scale=0.8,content=ft.Image(src="/icones/face_icon.png",scale=0.8), url="https://www.facebook.com/profile.php?id=100001617603914&mibextid=ZbWKwL",style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.BLUE,},side={ft.MaterialState.DEFAULT: ft.BorderSide(5, ft.colors.BLUE),ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),})),
                                                                ft.IconButton(content=ft.Image(src="/icones/link_icon.png",scale=0.8),scale=0.8, tooltip="LinkedIn",icon_color="blue",url="https://www.linkedin.com/in/gustavo-oliveira-25b422194/", style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.BLUE,},side={ft.MaterialState.DEFAULT: ft.BorderSide(5, ft.colors.BLUE),ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),}) ),
                                                                ft.IconButton(content=ft.Image(src="/icones/insta_icon.png",scale=0.8),scale=0.8 ,tooltip="Instagram", icon_color="blue",url="https://instagram.com/gut.oliveira?igshid=OGQ5ZDc2ODk2ZA==", style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.BLUE,},side={ft.MaterialState.DEFAULT: ft.BorderSide(5, ft.colors.BLUE),ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),})),
                                                            ]
                                                            
                                                            ),
                                                        
                                                        
                                                        
                                                    ]
                                                )
                                            )
                                    ]
                                )
                    ),

                    
                
                ]
                
            )
        )
        
        #Variaveis e lógicas
        
        box_service = Section_body_Service.content.controls
        box_projects = Section_body_projects.content.controls
            #Logica para adicionar dinamicamente os serviços
        for service in range(len(Servicos)):
            list_icon = list(Servicos.values())[service]["icon"]
            list_text = list(Servicos.values())[service]["text"]
            list_title = list(Servicos.values())[service]["title"]
            Card_Service = ft.Container(
                alignment=ft.alignment.center,
                margin=30,
                bgcolor="white",
                border_radius=ft.border_radius.all(20),
                width=600,
                height=400,
                col={"sm": 6, "md": 4, "xl": 4},
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.colors.BLACK,
                    offset=ft.Offset(0, 0),
                    blur_style=ft.ShadowBlurStyle.OUTER,
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        width=400,
                        height =150 ,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                
                                ft.ResponsiveRow(alignment=ft.alignment.center,controls=[
                                    
                                    ft.Icon(name=list_icon,size=70, color="blue")
                                ])
                                
                                ],
                            
                        )
                    ),
                    ft.Container(
                        alignment=ft.alignment.top_center,
                        width=400,
                        height=400,
                        content=ft.Column(
                            spacing=10,
                            alignment=ft.alignment.top_center,
                            controls=[
                            ft.ResponsiveRow(
                                controls=[
                                    ft.Text(value=list_title,weight="bold", size=17, text_align="center",font_family="OpenSans" , color="black" ),
                                    ft.Text(value=list_text, text_align="center", size=18, font_family="OpenSans" , color="black")
                                ]
                            )
                            
                            
                            ],
                        )
                    ),
                    
                    ]
                )
                    
            
        )
            
            box_service.append(Card_Service)

        #Logica para adicionar dinamicamente os projetos que trabalhei
        
        for projeto in range(len(Projetos)):
            
            
            
            
            list_data = list(Projetos.values())[projeto]["data"]
            list_type = list(Projetos.values())[projeto]["type"]
            list_image = list(Projetos.values())[projeto]["image"]
            list_text = list(Projetos.values())[projeto]["text"]
            list_title = list(Projetos.values())[projeto]["title"]
            
            
            
            Card_Projetos = ft.Container(
                margin=40,
                border_radius=20,
                alignment=ft.alignment.center,
                bgcolor="white",
                width=800,
                height=400,
                col={"sm": 6, "md": 6, "xl": 5},
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.colors.BLACK,
                    offset=ft.Offset(0, 0),
                    blur_style=ft.ShadowBlurStyle.OUTER,
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                    ft.Container(
                        alignment=ft.alignment.top_center,
                        width=800,
                        height =300 ,
                        content=ft.Column(
                            spacing=10,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                
                                
                                ft.Image(height=300,
                                        width=800, 
                                        fit=ft.ImageFit.FILL,
                                        src=list_image,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                        ),
                                
                                
                       
                                
                                ],
                            
                        )
                    ),
                    ft.Container(
                        padding=ft.padding.only(top=10, left=20),
                        alignment=ft.alignment.bottom_center,
                        width=800,
                        height=100,
                        content=ft.Column(
                            spacing=20,
                            controls=[
                            ft.Row(
                                spacing=30,
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                controls=[
                                    ft.Column([
                                        
                                        ft.Text(value=list_title, weight="bold", size=20, text_align="center", font_family="OpenSans" , color="black"),
                                    ft.Text(value=list_type+": ",weight="normal", size=17, text_align="center",font_family="OpenSans" , color="blue", spans=[ft.TextSpan(text=list_data,style=ft.TextStyle(color="black")) ]
                                    ),
                                        
                                        ]),
                                    
                                    ft.IconButton(icon=ft.icons.INFO_ROUNDED, icon_color="black", selected_icon_color="blue", tooltip=list_text, disabled=True)
                                    
                                    
                                    
                                ]
                            )
                            
                            
                            ],
                        )
                    ),
                    
                    ]
                )
                    
            
        )
            
            box_projects.append(Card_Projetos)
        
        # Funções
        
        #Conteudo da pagina
        content = ft.Column(
            controls=[

                
                ft.Stack(
                    key="HOME",
                    controls=
                    [
                ft.Image(src="/tech.jpg", fit=ft.ImageFit.CONTAIN, width=self.page.width,),
                
                ]
                    ),
                ft.ResponsiveRow(
                    controls=[
                        ft.Divider(color="transparent"),
                        Section_top_body,
                        ft.Divider(color="transparent"),
                        ft.Divider(color="transparent"),
                        ft.ResponsiveRow(alignment="center", controls=[
                            
                            ft.Text(value="SERVIÇOS", size=30, weight="bold", text_align="center", color="black", font_family="OpenSans" ),
                            ft.Text(value="Descrição de serviços que podem ser realizados", size=20, weight="normal", text_align="center", color="black", font_family="OpenSans"),
                            
                            ]),
                        ft.Divider(color="transparent"),
                        ft.Divider(color="transparent"),
                        ft.Divider(color="transparent"),
                        Section_body_Service,
                        ft.Divider(color="transparent"),
                        ft.Divider(color="transparent"),
                        ft.Divider(color="transparent"),
                        ft.ResponsiveRow(alignment="center", controls=[
                            
                            ft.Text(value="PROJETOS", size=30, weight="bold", text_align="center", color="black", font_family="Roboto"),
                            ft.Text(value="Descrição de projetos que já foram desenvolvidos ", size=20, weight="normal", text_align="center", color="black",font_family="Roboto"),
                            
                            ]),
                        ft.Divider(color="transparent"),
                        ft.Divider(color="transparent"),
                        Section_body_projects,
                        ft.Divider(color="transparent"),
                        ft.Divider(color="transparent"),
                        Section_body_contact
                    ]
                )
                
            ]
        )

        return content