#single inheritance
class animal():
    def __init__(self, name, sound) -> None:
        self._name = name;
        self._sound = sound;
    
    def animal_sound(self):
        print(f'{self._name} makes sound :', self._sound);

#animal == super()
class dog(animal):
    def __init__(self, name, sound, breed) -> None:
        super().__init__(name, sound);
        self._breed = breed;

    def dog_sound(self):
        return super().animal_sound();

ani = animal('cow', 'baaaaaa!');
ani.animal_sound();

d = dog('tommy', 'bhaubhau', 'husky');
d.dog_sound();

class cat(animal):
    def __init__(self, name, sound, breed) -> None:
        self._breed = breed;
        super().__init__(name, sound)

    #only specific for the cat class
    def cat_info(self):
        print(f'{self._name} makes {self._sound} : {self._breed}');

c = cat('biralo', 'meow meow', 'big biralo');
c.cat_info();

#multiple inheritances
class mother:
    def __init__(self, name, age) -> None:
        self.name = name;
        self.age = age;

    def show_info(self):
        print(f'{self.name} is mother of shiva. she is {self.age} years old');

class father:
    def __init__(self, fav_drinks, fav_food) -> None:
        self.drink = fav_drinks;
        self.food = fav_food;

    def show_info(self):
        print(f'{self.drink} is love by my father . he is {self.food} years old');

#inheriting more than two
class myself(father, mother):
    def __init__(self, name, age) -> None:
        super().__init__(name, age);


mom = mother('sarita', 45);
dad = father('arjun', 46);
me = myself('sarita', 45);
me.show_info();

#mro = method resolution order while defining the class 
print(myself.mro()); 

#multi level inheritance
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o = GoldenRetriever("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro());

##
class animal():
    #animal constructor
    def __init__(self, name, specis) -> None:
        self.name = name;
        self.specis = specis;

    def show_details(self):
        print(f'name :{self.name} \nspecis :{self.specis}');

class dog(animal):
    #dog constructor
    def __init__(self, name, specis, breed) -> None:
        self.breed = breed;
        #animal constructor
        animal.__init__(self, name, specis);

    def show_details(self):
        animal.show_details(self);
        print(f'breed :{self.breed}');

class husky(dog):
    #husky constructor
    def __init__(self, name, specis, breed, color) -> None:
        self.color = color;
        dog.__init__(self, name, specis, breed);

    #method overite by the dog
    def show_details(self):
        dog.show_details(self);
        print(f'color :{self.color}');

class_dog = husky('seti', 'dog', 'husky', 'white');
class_dog.show_details();

print('\n');
#example 2:
class grandfather():
    def __init__(self, grandfatherName, grandfatherAge) -> None:
        self.grandfatherName = grandfatherName;
        self.grandfatherAge = grandfatherAge;

    def details_grand(self):
        print(f'grandfather name : {self.grandfatherName} \ngrandfather age: {self.grandfatherAge}');

class father(grandfather):
    def __init__(self, fathername, fatherAge) -> None:
        self.fatherName = fathername;
        self.fatherAge = fatherAge;
        grandfather.__init__(self, grandfatherName = 'narayan', grandfatherAge = '90');
 
    def details_father(self):
        father.details_grand(self);
        print(f'father name :{self.fatherName} \nfather age :{self.fatherAge}');

class son(father):
    def __init__(self, sonname, sonage) -> None:
        self.sonname = sonname;
        self.sonage = sonage;
        father.__init__(self, fathername='arjun', fatherAge='47');

    def details_son(self):
        father.details_father(self);
        print(f'son name :{self.sonname} \nson age :{self.sonage}');

son_name = son('shiva', 18);
son_name.details_son();

#hierchial inheritance
class animal():
    def __init__(self, name, specis) -> None:
        self.name = name;
        self.specis = specis;

    def animal_info(self):
        print(f'name :{self.name} \nspecis :{self.specis}');

class dog(animal):
    def __init__(self, name, breed) -> None:
        self.breed = breed;
        animal.__init__(self, name, specis='dog');

    def dog_info(self):
        animal.animal_info(self);
        print(f'breed :{self.breed}');


class dog1(dog):
    def __init__(self, name, color) -> None:
        self.color = color;
        dog.__init__(self, name, breed = 'husky');

    def dog1_info(self):
        dog.dog_info(self);
        print(f'color :{self.color}');

class dog2(dog):
    def __init__(self, name, color) -> None:
        self.color = color;
        dog.__init__(self, name, breed = 'german sheffer');

    def dog2_info(self):
        dog.dog_info(self);
        print(f'color :{self.color}');

class cat(animal):
    def __init__(self, name, breed) -> None:
        self.breed = breed;
        animal.__init__(self, name, specis='cat');

    def cat_info(self):
        animal.animal_info(self);
        print(f'breed :{self.breed}');

class cat1(cat):
    def __init__(self, name, color) -> None:
        self.color = color;
        cat.__init__(self, name, breed='sphynx cat');

    def cat1_info(self):
        cat.cat_info(self);
        print(f'color :{self.color}');


class cat2(cat):
    def __init__(self, name, color) -> None:
        self.color = color;
        cat.__init__(self, name, breed='persian cat');

    def cat2_info(self):
        cat.cat_info(self);
        print(f'color :{self.color}');

print('\n')
dog_one = dog1('seti', 'white' );
dog_one.dog1_info();
print('\n')
dog_two = dog2('kali', 'black' );
dog_two.dog2_info();
        
print('\n')
cat_one = cat1('moana', 'white');
cat_one.cat1_info()
print('\n')
cat_two = cat2('sasha', 'black');
cat_two.cat2_info()

#hybrid inheritance 
class grand():
    def __init__(self, name, sex) -> None:
        self.name = name;
        self.sex = sex;

    def grand_info(self):
        print(f'name :{self.name} \nsex :{self.sex}');

class mother(grand):
    def __init__(self, name, age) -> None:
        self.age = age
        grand.__init__(self, name, sex='female');

    def mother_info(self):
        grand.grand_info(self);
        print(f'age :{self.age}');

class father(grand):
    def __init__(self, name, age) -> None:
        self.age = age;
        grand.__init__(self, name, sex='male');

    def father_info(self):
        grand.grand_info(self);
        print(f'age :{self.age}');

class son(mother, father):
    def __init__(self, name, hobby) -> None:
        self.hobby = hobby;
        mother.__init__(self, name, age = 18)
    
    def son_info(self):
        mother.mother_info(self);
        print(f'hobby :{self.hobby}');

class grand_child(son):
    def __init__(self, name, phn) -> None:
        self.phn = phn
        son.__init__(self, name, hobby='makeup artist');

    def grand_chi_info(self):
        son.son_info(self);
        print(f'phn number :{self.phn}');

print('\n');
anjelika = grand_child('anjelika', 9878665638);
anjelika.grand_chi_info();

        