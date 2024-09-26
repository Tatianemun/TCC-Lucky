define l = Character("Lucky")
define i = Character("Lily")
define r = Character("Rose")
define p = Character("Peter")
define a = Character("Ravi")
define g = Character("Gangue")

# The game starts here.

label start:
    
    scene flor
    with fade

    "Em um vilarejo encantado, Lucky, um pequeno duende, enfrenta dificuldades na escola devido ao bullying de Peter, um duende mais velho e maldoso."

    "No pátio, Lucky estava sozinho quando Peter apareceu, cercado por colegas"    
    scene patio
    show lucky at left
    show peter at center
    show gangue at right


    p "Olha só quem está aqui, o azarado do Lucky!"
    
    hide lucky
    show lucky_tenso at left

    p "E aí parceiro, tá querendo problemas?"

    l "Eu...Eu..."

    p "Olha só gente"
    p "Nem conseguir completar uma frase ele consegue"

    hide lucky_tenso
    show luckytriste at left

    g "hahahahahahahahahaha"


    hide luckytriste
    hide peter
    hide gangue
    "Você acha que Lucky deve confrontar Peter?"

menu:

    "Sim":
        jump sim

    "Não":
        jump nao

label sim:
    show lucky_serio2 at left
    show peter at center
    show gangue at right

    l "Quer saber, já estou cansado dessas suas provocações"
    l "Pare de querer bancar o valentão!"

    hide peter
    show peter_rindo
    p "He, he, he olha só rapazes, o Lucky ta se sentindo o tal"
    p "Virou piadista agora?"
    p "Se não quer ser motivo de piada, é melhor sair da minha frente!"

    hide lucky_serio2
    hide peter_rindo
    hide gangue


    "Lucky ficou abalado, mas um pouco mais confiante."
    jump principal

label nao:
    show lucky_tenso2 at left
    show peter at center
    show gangue at right

    p "Ih, olha lá!"
    p "O covarde decidiu fugir"

    hide lucky_tenso2
    hide peter

    show peter_rindo2 at left
    p "Aprendeu rapazes? É assim que temos que tratar esse tipo de gente"

    hide peter_rindo2
    hide gangue
    jump principal

label principal:
    scene flor
    show luckytriste at center
    "Lucky decide voltar para casa e para isso ele usa o caminho mais rápido: a floresta"


    scene casa
    show rose2 at left 
    show luckytriste2 at right

    "Ao chegar em casa, Lucky se depara com sua mãe"
    r "Ei, querido, você parece preocupado. O que aconteceu?"

    p "Peter está sempre me zoando na escola e não suporto mais isso."

    hide rose2
    hide luckytriste2

    "Lucky deve desabafar com sua mãe?"

menu:

    "Sim":
        jump bom

    "Não":
        jump ruim

label bom:

    show rose2 at left 
    show luckytriste2 at right

    l "Peter sempre está me incomodando e eu não fiz nada para ele"
    l "Hoje estava no pátio na hora do recreio e ele veio junto com os amigos deles me irritar"
    l "Não aguento mais isso"

    r "Isso acontece desde quando?"

    l "Já faz um tempo"

    r "Querido, devia ter me contado desde quando ele te incomodou da primeira vez"
    r "Saiba que eu vou estar sempre aqui e pode contar comigo"
    r "Depois vou ir na sua escola conversar com a diretora, tá bom?"

    l "Tá bom mãe, obrigado"

    r "Espero que Peter pare de vez de te incomodar"

    l "Também"
    jump alternativo


label ruim:

    show rose2 at left 
    show luckytriste2 at right
    r "Você falou com seus professores?"

    l "Não, mas não vai adiantar"
    l "Peter não respeita ninguém, aposto que se eu falar com os professores não vai dar em nada"
    l "Mas deixa isso pra lá"
    l "Não fique preocupada, uma hora ele para de me irritar"

    r "Não posso filho"
    r "Você está sofrendo e Peter tem que parar com essas provocações"
    r "Você vai falar com seus professores sobre essa situação e se for preciso vou na escola resolver"

    l "Ta bom"
    jump alternativo

label alternativo:
    show rose2 at left 
    show luckytriste2 at right

    l "Agora preciso esfriar a cabeça"
    
    r "Que tal um passeio?"

    l "Pode ser"
    l "Acho que vou explorar a floresta"

    r "Tá bom filho, toma cuidado lá fora"

    l "Ok, pode deixar"
    l "Tchau"

    r "Tchau"

    hide rose2
    hide luckytriste2

    scene flor
    "Ao explorar a floresta, Lucky encontra uma duende alegre"

    show lily2 at left
    show lucky2 at right

    i "Oi! Eu sou a Lily e você?"

    l "Oi, sou o Lucky"

    i "O que está fazendo aqui?"

    l "Vim passear e aproveitar para esfriar a cabeça"

    l "E você? Por que está na floresta?"

    i "Estou cuidando dos animais"
    i "Gosto de cuidar deles, dá uma paz"
    i "Além de fazer uma boa ação, me divirto fazendo isso"

    l "Que legal, realmente parece divertido"

    i "E é mesmo"
    i "Que tal me ajudar?"
    i "Assim podemos ficar conversando e brincar com os animais"
    
    hide lily2
    hide lucky2
    
    "Lucky deve ajudar Lily com os animais?"

menu:

    "Sim":
        jump otimo

    "Não":
        jump pessimo

label otimo:

    show lily2
    show lucky2

    l "Claro"
    l "Até acho ótimo para relaxar um pouco"
    l "E olha que realmente estou precisando"

    i "hahahaha você é engraçado"
    i "Mora aqui perto?"

    l "Sim e você?"

    i "Também"
    i "Estudo de amanhã, aí aproveitei essa tarde ensolarada para ficar com os animais"

    l "Que legal! Também estudo de manhã"

    i "Veio aproveitar esse sol também?"

    l "Na verdade, estou aqui para esquecer os problemas"
    l "A vida na escola não está muito fácil"

    i "Ué, o que aconteceu?"

    l "Tem um garoto que faz bullying comigo"
    l "Ele fica me incomodando junto com os amigos dele"
    l "Sabe isso me deixa muito triste"

    i "Te entendo, nunca sofri bullying mas fico tão indignada quando alguém sofre" 
    i "É horrivel como algumas pessoas se sentem no direito de fazer isso com os outros"

    l "Sim, o pior é que eles se sentem bem em ter esse comportamento"

    i "Sim"
    i "Você já falou isso com alguém?" 

    l "Sim, com a minha mãe"  
    l "Ela me ajudou e disse que vai falar com a escola"

    i "Ah, é sempre bom ter alguém para conversar"

    l "Sim"

    i "Você já falou com o seus professores?"
    i "Em situações como essa, é sempre bom avisar eles"

    l "Sei que é bom, mas não falei"
    l "Tenho medo de falar e piorar as coisas"
    l "E se eles começarem a me zoar ainda mais?!"
    
    i "Sei que você tem motivo para ter medo, mas se você não contar, pode ser pior"

    l "Verdade"
    l "Só fico pensando que se eu falar, vão me achar fraco"

    i "Não, Lucky!"
    i "Pedir ajuda não é sinal de fraqueza, é de coragem"
    i "Olha, você não está sozinho. Sua mãe está do seu lado e agora, eu também"

    l "Sabe, gostaria de me expressar melhor"

    i "Te entendo, tive esse problema e o que me ajudou foi o teatro, acho que pode te ajudar também"

    l "Será?"

    i "Sim, ele ajuda a desenvolver o autoconhecimento, a autoestima e a comunicação"

    l "Vou pensar nisso"
    l "Talvez me juntar a um grupo de teatro me faça bem"

    i "Com certeza!"
    i "Desenvolver a autoestima vai fazer você se valorizar e dessa forma os comentários negativos não vão te afetar"

    l "Verdade"
    l "Às vezes, me sinto tão inseguro que acabo acreditando nas coisas ruins que eles falam de mim"

    i "Sim, infelizmente isso acontece com muita gente"
    i "Mas saiba que a coragem vem de dentro"





    "Lucky ajuda Lily, e durante o trabalho, eles conversam sobre coragem e autoestima. Lily diz que a bondade de Lucky é seu verdadeiro poder. Lucky começa a se sentir mais confiante e reconectado consigo mesmo."
    jump continuacao

label pessimo:
    "Lucky agradece a oferta, mas decide seguir seu caminho sozinho pela floresta. Ele se sente um pouco perdido, sem saber ao certo o que fazer para lidar com seus problemas. A solidão o deixa mais reflexivo."
    jump continuacao

label continuacao:
    scene festa
    show peter2 at left
    show lucky at right
    "Durante a festa, Peter tenta zombar de Lucky novamente."

    hide peter2
    hide lucky

    show peter2 at left
    show luckytriste2 at right

    p "Olha só, o azarado de novo!"

    hide peter2
    hide luckytriste2

    "Lucky deve responder a Peter?"

menu:

    "Sim":
        jump confiante 

    "Não":
        jump humilhei

label confiante:
    show lucky at center
    "Lucky se levanta com confiança e responde que ele não é azarado, mas sim um duende bondoso e corajoso. Os outros duendes começam a admirar sua atitude, e Peter percebe que suas provocações não estão funcionando mais"
    jump finalfeliz

label humilhei:
    "Lucky permanece em silêncio, mas Lily e Ravi, que estão com ele, o defendem. Peter se surpreende com a solidariedade dos amigos de Lucky e começa a perceber que está isolado em suas provocações"
    jump finaltriste

label finalfeliz:
    "Peter, tocado pela coragem e bondade de Lucky, se aproxima com sinceridade"

    p "Desculpe por ter sido tão cruel"

    p "Eu não devia ter te tratado assim"

    p "Me desculpe pelas minhas atitudes"

    l "Tudo bem, podemos começar de novo?"

    p "Claro"

    "Peter, agora amigo, se junta a Lucky, Lily e Ravi. Eles brincam juntos na floresta, e Lucky sente que encontrou seu valor e seu lugar no mundo, transformando sua situação com coragem e bondade"

label finaltriste:
    "Peter continua sendo rude e Lucky percebe que não precisa de aprovação de Peter para ser feliz"

    
    "Lucky, Lily e Ravi saem juntos, deixando Peter para trás. Lucky percebe que sua confiança não depende da opinião dos outros, mas sim de sua própria força interior"

    return
