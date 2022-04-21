car [a-zA-Z]
dig [0-9]
%%                     
[ \t]+                          { /*Detecta espacios y los filtra*/ }
[ \n]                           { return 0; }
{car}({car})*                   { if(yyleng <= 2){ printf("id %40s\n", yytext); } else{ printf("no_reconocido %29s\n", yytext); }}
"+"|"-"                         { printf("op %40c\n", yytext[0]); }
{dig}+                          { printf("int %39d\n", atoi(yytext)); }
.                               { printf("no_reconocido %29c\n", yytext[0]); }
%%
//Pruebas: 43-9+3 - ab + 8 - c, a+  10 - 7, a+3-ab+@-abc
//Nombre: Hernández Vázquez Israel
int main(int argc, char ** argv)
{
    printf("Ingrese la cadena a analizar: ");
    yylex();
    printf("|  Tipo Token  |                   |  Token  |\n");   
    exit(0);
}