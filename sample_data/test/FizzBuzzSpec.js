describe('Desafio FizzBuzz', function() {

    describe('Fizz', function(){

        it('Deve retornar Fizz quando a entrada for 3', function() {
            expect(FizzBuzz(3)).toBe('Fizz');
        });

        it('Deve retornar Fizz quando a entrada for 9', function() {
            expect(FizzBuzz(9)).toBe('Fizz');
        });

    });

    describe('Buzz', function(){        

        it('Deve retornar Buzz quando a entrada for 5', function() {
            expect(FizzBuzz(5)).toBe('Buzz');
        });

        it('Deve retornar Buzz quando a entrada for 25', function() {
            expect(FizzBuzz(25)).toBe('Buzz');
        });

    });

    describe('FizzBuzz', function(){

        it('Deve retornar FizzBuzz quando a entrada for 15', function() {
            expect(FizzBuzz(15)).toBe('FizzBuzz');
        });

        it('Deve retornar FizzBuzz quando a entrada for 30', function() {
            expect(FizzBuzz(30)).toBe('FizzBuzz');
        });

    });

    describe('Não é divisível por 3 ou 5', function(){

        it('Deve retornar 2 quando a entrada for 2', function (){
            expect(FizzBuzz(2)).toBe(2);
        });

        it('Deve retornar 4 quando a entrada for 4', function(){
            expect(FizzBuzz(4)).toBe(4);
        });

    });

});