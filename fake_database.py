from prompt import CompanyDetails


digiornos = CompanyDetails("Digiornos", 
                           "A classic italian restaurant. We take pride in delivering the best pizza for the best prices with the best service.", 
                           "customerservice@digiornos.com")


youbanhmi = CompanyDetails("You Banh Mi", 
                           "Traditional vietnamese dishes with a modern twist. Come hungry, leave happy!", 
                           "customerservice@youbanhmi.com")


fake_database = {"Digiornos": digiornos, "youbanhmi": youbanhmi}
