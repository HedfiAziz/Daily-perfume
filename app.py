
from flask import Flask, render_template, abort, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'cle_secrete_luxe_daily_perfume' # Nécessaire pour afficher les messages de confirmation


# BASE DE DONNÉES DU CATALOGUE (Haute Parfumerie)
PRODUCTS = {
    # ==========================================
    # 1. COLLECTION PARFUMS
    # ==========================================
    'floreal': {
        'name': 'Floréal',
        'category': 'Pour Femme',
        'type': 'Eau de Parfum Intense',
        'size': '50 ml',
        'main_image': 'Parfums images/floréal.jpg',
        'description': 'Une création lumineuse et audacieuse où la délicatesse des fleurs blanches rencontre la force d\'un sillage boisé. Un hommage contemporain à la féminité absolue.',
        'top_notes': 'Bergamote de Calabre, Bourgeon de Cassis',
        'heart_notes': 'Absolu de Rose de Mai, Jasmin Impérial',
        'base_notes': 'Musc Blanc, Bois de Cèdre de Virginie',
        'ingredients': 'Alcohol Denat., Parfum (Fragrance), Aqua (Water), Benzyl Salicylate, Linalool, Hydroxycitronellal, Limonene, Geraniol.',
        'gallery_images': ['Parfums images/floreal-fb1.jpg', 'Parfums images/floreal-fb2.png', 'Parfums images/floreal-fb3.png']    
    },

    'pure-vanille': {
        'name': 'Pure Vanille',
        'category': 'Pour Femme',
        'type': 'Eau de Parfum Intense',
        'size': '50 ml',
        'main_image': 'Parfums images/pure-vanille.jpg',
        'description': 'Une interprétation riche, charnelle et profondément enveloppante de la gousse de vanille. Un équilibre parfait entre douceur gourmande et sensualité mystérieuse.',
        'top_notes': 'Fleur d\'Oranger, Accord Amandé',
        'heart_notes': 'Gousse de Vanille Bourbon, Héliotrope',
        'base_notes': 'Ambre Noir, Absolu de Benjoin',
        'ingredients': 'Alcohol Denat., Parfum (Fragrance), Aqua (Water), Coumarin, Vanillin, Benzyl Benzoate, Anise Alcohol.',
        'gallery_images': ['Parfums images/Purevanille-fb1.jpg', 'Parfums images/Purevanille-fb2.png', 'Parfums images/Purevanille-fb3.png']
    },

    'rose-verde': {
        'name': 'Rose Verde',
        'category': 'Pour Femme',
        'type': 'Eau de Parfum Intense',
        'size': '50 ml',
        'main_image': 'Parfums images/rose-verde.jpg',
        'description': 'La fraîcheur d\'une rose matinale cueillie à l\'aube, mêlée à des notes vertes croquantes et acidulées. Une fragrance vive, pure et intensément rafraîchissante.',
        'top_notes': 'Menthe Froissée, Essence de Citron vert',
        'heart_notes': 'Pétales de Rose Turque, Thé Vert',
        'base_notes': 'Feuilles de Figuier, Muscs Transparents',
        'ingredients': 'Alcohol Denat., Parfum (Fragrance), Aqua (Water), Citronellol, Alpha-Isomethyl Ionone, Citral, Eugenol.',
        'gallery_images': ['Parfums images/roseverde1.jpg', 'Parfums images/roseverde2.jpg', 'Parfums images/roseverde3.png']
    },

    'gentlemens-code': {
        'name': "Gentlemen's Code",
        'category': 'Pour Homme',
        'type': 'Eau de Parfum Intense',
        'size': '50 ml',
        'main_image': "Parfums images/gentlemen's-code.jpg",
        'description': 'La signature de l\'homme moderne raffiné. Un accord cuiré puissant subtilement contrasté par la fraîcheur des agrumes nobles et la chaleur des épices.',
        'top_notes': 'Pamplemousse Noir, Cardamome du Guatemala',
        'heart_notes': 'Feuille de Violette, Accord Cuir Brut',
        'base_notes': 'Essence de Patchouli, Vétiver de Haïti',
        'ingredients': 'Alcohol Denat., Parfum (Fragrance), Aqua (Water), Limonene, Coumarin, Linalool, Citonellol, Benzyl Cinnamate.',
        'gallery_images': ['Parfums images/glm1.jpg', 'Parfums images/glm2.jpg', 'Parfums images/glm3.png']
    },

    'the-king': {
        'name': 'The King',
        'category': 'Pour Homme',
        'type': 'Eau de Parfum Intense',
        'size': '50 ml',
        'main_image': 'Parfums images/the-king.jpg',
        'description': 'Un parfum souverain d\'une puissance magnétique. Les bois précieux les plus rares s\'unissent dans une symphonie majestueuse pour marquer les esprits.',
        'top_notes': 'Poivre Rose, Safran d\'Iran',
        'heart_notes': 'Bois d\'Aoud Secret, Cèdre de l\'Atlas',
        'base_notes': 'Santal Crémeux, Cuir Noir, Tabac blond',
        'ingredients': 'Alcohol Denat., Parfum (Fragrance), Aqua (Water), Linalool, Limonene, Eugenol, Farnesol, Isoeugenol.',
        'gallery_images': ['Parfums images/king1.jpg', 'Parfums images/king2.jpg', 'Parfums images/king3.jpg']
    },

    'glow-addiction': {
        'name': 'Glow Addiction',
        'category': 'Collection Privée • Unisexe',
        'type': 'Eau de Parfum Intense',
        'size': '50 ml',
        'main_image': 'Parfums images/glow-addiction.jpg',
        'description': 'Un sillage charnel et lumineux pensé comme une seconde peau. Une addiction olfactive immédiate construite autour d\'effluves ambrées et solaires.',
        'top_notes': 'Note Solaire, Bergamote Confite',
        'heart_notes': 'Ylang-Ylang des Comores, Fleur de Tiaré',
        'base_notes': 'Ambre Gris, Gousse de Vanille, Noix de Coco',
        'ingredients': 'Alcohol Denat., Parfum (Fragrance), Aqua (Water), Benzyl Salicylate, Linalool, Benzyl Alcohol, Benzyl Benzoate.',
        'gallery_images': ['Parfums images/glow1.jpg', 'Parfums images/glow2.jpg', 'Parfums images/glow3.png']
    },

    'pure-sensation': {
        'name': 'Pure Sensation',
        'category': 'Unisexe',
        'type': 'Eau de Parfum Intense',
        'size': '50 ml',
        'main_image': 'Parfums images/pure-sensation.jpg',
        'description': 'Un frisson de pureté absolue. Une rencontre contrastée entre une fraîcheur glaciale cristalline et la profondeur texturée de notes orientales modernes.',
        'top_notes': 'Menthe Poivrée, Aldéhydes Givrés',
        'heart_notes': 'Encens Mystique, Iris de Florence',
        'base_notes': 'Musc Liquide, Bois de Cachemire',
        'ingredients': 'Alcohol Denat., Parfum (Fragrance), Aqua (Water), Alpha-Isomethyl Ionone, Coumarin, Limonene.',
        'gallery_images': ['Parfums images/pure1.jpg', 'Parfums images/pure2.jpg', 'Parfums images/pure3.png']
    },
    
    # ==========================================
    # 2. COLLECTION MUSCS
    # ==========================================
    'musc-blanc': {
        'name': 'Musc Blanc',
        'category': 'Huile de Parfum',
        'type': 'Concentré de Parfum Pur',
        'size': 'Elixir',
        'main_image': 'Musc images/Musc-Blanc.jpg',
        'description': 'L\'essence même de la pureté traditionnelle. Une texture d\'huile riche et veloutée qui fusionne avec la peau pour diffuser une odeur de propre, réconfortante et éternelle.',
        'top_notes': 'Note Poudrée, Accord Coton',
        'heart_notes': 'Fleur de Lotus, Rose Blanche',
        'base_notes': 'Musc Blanc Intense, Ambre Doux',
        'ingredients': 'Parfum (Fragrance Concentrated Oil), Alpha-Isomethyl Ionone, Coumarin, Citonellol, Hexyl Cinnamal.',
        'gallery_images': ['Musc images/mb1.jpg', 'Musc images/mb2.jpg', 'Musc images/mb3.png']
    },

    'musc-grenade': {
        'name': 'Musc Grenade',
        'category': 'Huile de Parfum',
        'type': 'Concentré de Parfum Pur',
        'size': 'Elixir',
        'main_image': 'Musc images/Musc-Grenade.jpg',
        'description': 'Une déclinaison audacieuse et fruitée de notre élixir signature. L\'acidité gourmande de la grenade juteuse réveille la douceur soyeuse du musc traditionnel.',
        'top_notes': 'Grenade Noire, Baies Rouges',
        'heart_notes': 'Pêche Blanche, Pivoine Rose',
        'base_notes': 'Musc Soyeux, Vanille Givrée',
        'ingredients': 'Parfum (Fragrance Concentrated Oil), Limonene, Linalool, Hydroxycitronellal.',
        'gallery_images': ['Musc images/mg1.jpg', 'Musc images/mg2.jpg', 'Musc images/mg3.jpg']
    },

    # ==========================================
    # 3. COLLECTION PARFUMS D'AMBIANCE
    # ==========================================
    'ambiance-fraicheur-pins': {
        'name': 'Fraîcheur de Pins',
        'category': 'Parfum d\'intérieur',
        'type': 'Spray d\'Ambiance',
        'size': '200 ml',
        'main_image': 'Ambiance images/fraicheur-pins.jpg',
        'description': 'L\'essence pure de la nature. Une balade revigorante au cœur d\'une forêt de conifères. Ce spray purifie l\'air et apporte une bouffée d\'oxygène boisée et résineuse dans vos espaces.',
        'top_notes': 'Aiguilles de Pin, Sève Froide',
        'heart_notes': 'Eucalyptus, Écorce de Cèdre',
        'base_notes': 'Mousse de Chêne, Vétiver',
        'ingredients': 'Alcool de parfumerie purifié, Eau distillée, Concentré de parfum premium.',
        'gallery_images': ['Ambiance images/all.jpg'] 
    },

    'ambiance-douceur-fruitee': {
        'name': 'Douceur Fruitée',
        'category': 'Parfum d\'intérieur',
        'type': 'Spray d\'Ambiance',
        'size': '200 ml',
        'main_image': 'Ambiance images/douceur-fruitee.jpg',
        'description': 'Doux. Fruité. Irrésistible. Un cocktail ensoleillé et vitaminé qui diffuse une joie de vivre immédiate. Idéal pour créer une atmosphère chaleureuse et pétillante dans votre salon.',
        'top_notes': 'Pamplemousse Rose, Écorce d\'Orange',
        'heart_notes': 'Nectar de Mangue, Pêche Blanche',
        'base_notes': 'Musc Fruité, Sucre de Canne',
        'ingredients': 'Alcool de parfumerie purifié, Eau distillée, Concentré de parfum premium.',
        'gallery_images': ['Ambiance images/all.jpg'] 
    },

    'ambiance-rose-boisee': {
        'name': 'Rose Boisée',
        'category': 'Parfum d\'intérieur',
        'type': 'Spray d\'Ambiance',
        'size': '200 ml',
        'main_image': 'Ambiance images/rose-boisee.jpg',
        'description': 'La douceur d\'une élégance boisée. Le mariage parfait et sophistiqué entre la délicatesse d\'une rose veloutée et le caractère profond et rassurant des bois précieux.',
        'top_notes': 'Pétales de Rose, Poivre Rose',
        'heart_notes': 'Rose de Damas, Géranium',
        'base_notes': 'Bois de Santal, Oud Léger',
        'ingredients': 'Alcool de parfumerie purifié, Eau distillée, Concentré de parfum premium.',
        'gallery_images': ['Ambiance images/all.jpg'] 
    },

    'ambiance-nectar-ete': {
        'name': 'Nectar D\'été',
        'category': 'Parfum d\'intérieur',
        'type': 'Spray d\'Ambiance',
        'size': '200 ml',
        'main_image': 'Ambiance images/nectar-ete.jpg',
        'description': 'La fraîcheur naturelle qui illumine vos espaces. Une brise estivale herbacée et citronnée qui balaie les mauvaises odeurs pour laisser place à une pureté éclatante.',
        'top_notes': 'Zeste de Citron, Feuilles de Menthe',
        'heart_notes': 'Fleurs Blanches, Herbe Coupée',
        'base_notes': 'Bois Blancs, Musc Propre',
        'ingredients': 'Alcool de parfumerie purifié, Eau distillée, Concentré de parfum premium.',
        'gallery_images': ['Ambiance images/all.jpg'] 
    },

    'ambiance-douceur-sucree': {
        'name': 'Douceur Sucrée',
        'category': 'Parfum d\'intérieur',
        'type': 'Spray d\'Ambiance',
        'size': '200 ml',
        'main_image': 'Ambiance images/douceur-sucree.jpg',
        'description': 'Sucré. Envoûtant. Inoubliable. Une atmosphère gourmande et réconfortante qui transforme votre maison en un cocon moelleux et irrésistible.',
        'top_notes': 'Macaron, Amande Douce',
        'heart_notes': 'Jasmin Sucré, Vanille Bourbon',
        'base_notes': 'Caramel Fondant, Praline',
        'ingredients': 'Alcool de parfumerie purifié, Eau distillée, Concentré de parfum premium.',
        'gallery_images': ['Ambiance images/all.jpg'] 
    },

    # ==========================================
    # 4. COLLECTION PARFUMS DE VOITURE (Les 5 Senteurs)
    # ==========================================
    'voiture-fraicheur-pins': {
        'name': 'Diffuseur Voiture - Fraîcheur de Pins',
        'category': 'Parfum de Voiture',
        'type': 'Huile Essentielle Suspendue',
        'size': 'Flacon Diffuseur',
        'main_image': 'Voiture images/voiture-fraicheur-pins.jpg',
        'description': 'Votre voiture mérite une odeur délicieuse (كرهبتك تستاهل ريحة بنينة) ! L\'essence pure de la nature vous accompagne sur la route. Un design élégant en bois véritable qui diffuse subtilement des notes boisées pour purifier l\'habitacle.',
        'top_notes': 'Aiguilles de Pin, Sève Froide',
        'heart_notes': 'Eucalyptus, Écorce de Cèdre',
        'base_notes': 'Neutralisation des odeurs, Longue durée (45 jours)',
        'ingredients': 'Huiles parfumées hautement concentrées, 0% alcool pour une évaporation lente par capillarité.',
        'gallery_images': ['Voiture images/all.jpg'] 
    },

    'voiture-douceur-fruitee': {
        'name': 'Diffuseur Voiture - Douceur Fruitée',
        'category': 'Parfum de Voiture',
        'type': 'Huile Essentielle Suspendue',
        'size': 'Flacon Diffuseur',
        'main_image': 'Voiture images/voiture-douceur-fruitee.jpg',
        'description': 'Votre voiture mérite une odeur délicieuse (كرهبتك تستاهل ريحة بنينة) ! Un cocktail ensoleillé et vitaminé pour vos trajets quotidiens. Ce flacon suspendu diffuse une joie de vivre irrésistible dans votre véhicule.',
        'top_notes': 'Pamplemousse Rose, Écorce d\'Orange',
        'heart_notes': 'Nectar de Mangue, Pêche Blanche',
        'base_notes': 'Neutralisation des odeurs, Longue durée (45 jours)',
        'ingredients': 'Huiles parfumées hautement concentrées, 0% alcool pour une évaporation lente par capillarité.',
        'gallery_images': ['Voiture images/all.jpg'] 
    },

    'voiture-rose-boisee': {
        'name': 'Diffuseur Voiture - Rose Boisée',
        'category': 'Parfum de Voiture',
        'type': 'Huile Essentielle Suspendue',
        'size': 'Flacon Diffuseur',
        'main_image': 'Voiture images/voiture-rose-boise.jpg',
        'description': 'Votre voiture mérite une odeur délicieuse (كرهبتك تستاهل ريحة بنينة) ! La douceur d\'une élégance boisée voyage avec vous. Un parfum sophistiqué qui transforme l\'habitacle de votre voiture en un salon de luxe.',
        'top_notes': 'Pétales de Rose, Poivre Rose',
        'heart_notes': 'Rose de Damas, Géranium',
        'base_notes': 'Neutralisation des odeurs, Longue durée (45 jours)',
        'ingredients': 'Huiles parfumées hautement concentrées, 0% alcool pour une évaporation lente par capillarité.',
        'gallery_images': ['Voiture images/all.jpg'] 
    },

    'voiture-nectar-ete': {
        'name': 'Diffuseur Voiture - Nectar D\'été',
        'category': 'Parfum de Voiture',
        'type': 'Huile Essentielle Suspendue',
        'size': 'Flacon Diffuseur',
        'main_image': 'Voiture images/voiture-nectar-ete.jpg',
        'description': 'Votre voiture mérite une odeur délicieuse (كرهبتك تستاهل ريحة بنينة) ! Une fraîcheur naturelle qui illumine vos trajets. Idéal pour balayer les mauvaises odeurs de tabac ou d\'humidité et laisser une pureté éclatante.',
        'top_notes': 'Zeste de Citron, Feuilles de Menthe',
        'heart_notes': 'Fleurs Blanches, Herbe Coupée',
        'base_notes': 'Neutralisation des odeurs, Longue durée (45 jours)',
        'ingredients': 'Huiles parfumées hautement concentrées, 0% alcool pour une évaporation lente par capillarité.',
        'gallery_images': ['Voiture images/all.jpg'] 
    },

    'voiture-douceur-sucree': {
        'name': 'Diffuseur Voiture - Douceur Sucrée',
        'category': 'Parfum de Voiture',
        'type': 'Huile Essentielle Suspendue',
        'size': 'Flacon Diffuseur',
        'main_image': 'Voiture images/voiture-douceur-sucree.jpg',
        'description': 'Votre voiture mérite une odeur délicieuse (كرهبتك تستاهل ريحة بنينة) ! Une atmosphère gourmande et réconfortante pour affronter les embouteillages avec le sourire. Sucré, envoûtant et inoubliable.',
        'top_notes': 'Macaron, Amande Douce',
        'heart_notes': 'Jasmin Sucré, Vanille Bourbon',
        'base_notes': 'Neutralisation des odeurs, Longue durée (45 jours)',
        'ingredients': 'Huiles parfumées hautement concentrées, 0% alcool pour une évaporation lente par capillarité.',
        'gallery_images': ['Voiture images/all.jpg'] 
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # 1. On récupère les données tapées par le client
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # 2. Pour l'instant, on affiche le message dans la console de ton terminal (pour vérifier que ça marche)
        print("="*50)
        print("NOUVEAU MESSAGE REÇU !")
        print(f"De : {name} ({email})")
        print(f"Sujet : {subject}")
        print(f"Message : {message}")
        print("="*50)

        # 3. On envoie un beau message de succès au client
        flash("Votre message a été envoyé avec succès. Nos experts vous répondront sous 24 heures.", "success")
        
        # 4. On recharge la page pour vider le formulaire
        return redirect(url_for('contact'))

    return render_template('contact.html')

# ROUTE DYNAMIQUE SENIOR POUR LES PRODUITS
@app.route('/produit/<product_id>')
def product_detail(product_id):
    product = PRODUCTS.get(product_id)
    if not product:
        abort(404)
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True, port=3000)