# LSD-support-extension

Welcome to the `LSD:Lindenmayer-System-Drawing` extension! This extension provides support for `.lsystem` files, allowing you to write, visualize, and compile L-systems directly within VS Code.

- [LSD-support-extension](#lsd-support-extension)
- [LSD:Lindenmayer-System-Drawing VS Code Extension](#lsdlindenmayer-system-drawing-vs-code-extension)
    - [Overview](#overview)
    - [Installation](#installation)
    - [Features](#features)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [Compiling L-Systems](#compiling-l-systems)
    - [Support and Contributions](#support-and-contributions)
    - [License](#license)
- [About LSD: The L-system language.](#about-lsd-the-l-system-language)
  - [Language syntax](#language-syntax)
    - [Internal types of the language:](#internal-types-of-the-language)
    - [Reserved words:](#reserved-words)
    - [Declaration of an l-System](#declaration-of-an-l-system)
      - [Symbols allowed in rule declaration](#symbols-allowed-in-rule-declaration)
    - [Change the axiom of an already defined L-System](#change-the-axiom-of-an-already-defined-l-system)
    - [Add a rule to an already defined L-System](#add-a-rule-to-an-already-defined-l-system)
    - [Canvas Statement](#canvas-statement)
    - [To draw L-Systems!](#to-draw-l-systems)
    - [Operations on types](#operations-on-types)
    - [Assignment and Creation of variables](#assignment-and-creation-of-variables)
    - [Conditionals:](#conditionals)
    - [Cycles:](#cycles)
    - [Program execution:](#program-execution)
  - [Compiler Architecture](#compiler-architecture)
    - [Lexer:](#lexer)
    - [Parser:](#parser)
    - [Semantic verification:](#semantic-verification)

# LSD:Lindenmayer-System-Drawing VS Code Extension

### Overview

**Name**: `LSD:Lindenmayer-System-Drawing`  
**Description**: This extension facilitates the compilation of `.lsystem` files for visualization of L-system drawings.   
**Version**: `1.0.0`  
**Maintainers**: sheyls, dalfonso44, JLeiva44 

The `LSD:Lindenmayer-System-Drawing` extension offers language support for `.lsystem` files. This means that the content of these files must follow a specific syntax [(see the lsd lenguage section)](#about-lsd-the-l-system-language), allowing them to accurately represent and visualize L-Systems.

![Extension Icon](icon.png)

### Installation

1. Open **VS Code**.
2. Navigate to the **Extensions** view by clicking on the square icon on the sidebar.
3. Search for **LSD:Lindenmayer-System-Drawing**.
4. Click **Install**.

> **Note**: Ensure that you have VS Code version `^1.75.0` or later.

### Features

- **Syntax Highlighting**: Supports `.lsystem` files to provide a colorful and meaningful representation of the content.
- **Compilation**: Allows users to compile `.lsystem` files to draw L-Systems.

## Configuration

To utilize the integrated LSD compiler:

1. Clone or download this repository to your local machine.
2. Navigate to **File > Preferences > Settings** or use the shortcut `Ctrl + ,`.
3. In the search bar, enter `LSD: Lindenmayer-System-Drawing`.
4. Look for the `lsd.compilerRoot` setting.
5. Provide the path to the `compiler` directory inside the cloned/downloaded repository.

This sets the root for the bundled LSD compiler, allowing you to compile `.lsystem` files directly from Visual Studio Code.

## Usage

### Compiling L-Systems

1. Open any `.lsystem` file.
2. Click the "Compile L-system" button on the top-right corner of the editor window.
3. If configured correctly, this will compile the `.lsystem` file and produce the appropriate L-System drawing.

### Support and Contributions

For support, questions, or contributions, please head over to our [GitHub repository](https://github.com/sheyls/LSD-Lindenmayer-System-Drawing). Here, you can raise issues or submit pull requests.

### License

This extension is licensed under the [MIT LICENSE](LICENSE).

---


# About LSD: The L-system language.

LSD is a DSL :) that aims to visualize L-Systems. An L-System or Lindenmayer system is a formal grammar (a set of rules and symbols) primarily used to model the plant growth process; It can also model the morphology of a variety of organisms. They can also be used to generate self-similar fractals such as iterated function systems. L-systems were introduced and developed in 1968 by the Hungarian biologist and theoretical botanist Aristid Lindenmayer.

## Language syntax
Statically typed language, not object-oriented.

### Internal types of the language:

`lsys` - represents an L-System
`int` - represents a 32-bit integer
`float` - represents a float
`string` - represents a string of characters (Always uppercase)
`brush` - represents a brush for drawing
`canvas` - represents a canvas for drawing
`color` - represents a color (in hexadecimal)
`bool` - true | false


### Reserved words:
-`canvas`
-`draw`
-`brush`
-`lsys`
-`axiom`
-`color`
-`size`
-`speed`
-`high`
-`width`
-`if`
-`else`
-`bool`
-`true`
-`false`
-`int`
-`string`
-`addRule`
-`repeat`

### Declaration of an l-System

**Definition:**

```
lsys <system_name> {
     axiom: <representative_character>,
     <right_part_of_the_ruler> => <left_part_of_the_ruler>,
     ...
     <right_part_of_the_ruler> => <left_part_of_the_ruler>,
}

```
***Example:**

```
lsys leaf {
     axiom: A,
     F => >F<,
     A => F[+X]FB,
     B => F[-Y]FA,
     X => A,
     Y => B
};

```
#### Symbols allowed in rule declaration

| Symbol | Action associated with the brush |
| ------------- | ------------------------------------ |
| f | Moves forward painting |
| g | Moves forward without painting |
| + | Turn left the indicated angle |
| - | Turn right the indicated angle |
| [ | Adds the current state of the drawing (brush position and rotation angle) to the stack |
| ] | Pops the last state onto the stack and takes it as current |
| # | Increase line thickness |
| ! | Decrease the thickness of the line |
| > | Multiply the length of the line by a factor |
| < | Divide the length of the line by a factor |
| & | Change the meaning of the + and -|
| % | Increases the turning angle |
| $ | Decreases the turning angle |

### Change the axiom of an already defined L-System

**Definition:**

```
change_axiom( <system_name>, <new_axiom>);

```
**Example:**

```
change_axiom( leaf, AC );

```
### Add a rule to an already defined L-System

**Definition:**

```
add_rule( <system_name>, <right_part_of_rule> => <left_part_of_rule> );

```
**Example:**

```
add_rule(leaf, C => FF );

```

###Brushes statement

**Definition:**

```
brush <brush_name> {
     size: <int>,
     color: <color>,
     speed: <int>

}

*size* - Describes the width of the brush line
*speed* - Describes the speed at which the brush draws
```
**Example:**

```

brush small_blue {

     size: 1,
     color: #40e0d0,
     speed: 300

};

brush breig_d {

     size: 5.
     color: #ff0000,
     speed: 300

};


```

### Canvas Statement

**Definition:**

```
canvas <brush_name> {

     high: <int>,
     width: <int>,
     color: <color>

}
```
**Example:**

```
canvas soft_orange {

     high: 4000,
     width: 4000,
     color: #ffebcd
};

```

### To draw L-Systems!

**Definition:**

```python
draw( <lsys>, <brush>, <canvas>, <line_length>, <rotation_angle>, <system_complexity>)
```


**Example:**

```python
draw(leaf, small_blue, soft_orange, 5, 35, 5);

```

### Operations on types

| Symbol | Meaning |
| ------------- | --------------- |
| (+) | Standard sum |
| (-) | Standard Subtraction |
| (<) | Less than |
| (>) | Greater than |
| >= | Greater equal|
| <= | Lesser equal |
| == | Same |
| != | Different |

All operations are defined on int and float types.
Equality and inequality operators are also defined for `strings` and `bool`.

### Assignment and Creation of variables
 
  ```
int a = 5;

draw(leaf, small_blue, soft_orange, a, 35, a);

a = 6;

repeat a {
     draw(leaf, small_blue, soft_orange, 7, 35, 5);
};
---------------------------------------------

bool b = true;

if (b) {
     draw(leaf, mybrush, mycanvas, 5 ,45, 8);
     b = false;
};

-------------------------------------------

string c = FF+;

if (c == FF+) {
     draw(leaf, mybrush, mycanvas, 5 ,45, 8);
};

-------------------------------------------

Colors will always be entered in hexadecimal notation. The *hexadecimal_colors* pdf is attached for consultation.

cabbage white = #ffffff;

brush mybrush {

     size: 1,
     color: white,
     speed: 500

};

  ```

### Conditionals:


**Example:**

```python
if (a == 6) {
     draw(leaf, small_blue, soft_orange, a ,45, a)
};

if ( a (+) 1 == 7 ) {
     draw(leaf, small_blue, soft_orange, 5 ,45, 8);
} else { draw(star, big_red, soft_orange, 7 ,45, 3); };

```

### Cycles:

**Definition:**

```python
repeat <int> {
     <instructions>;
};

```

**Example:**

```python
int a = 5;

repeat a{

     draw(quedratic_gosper, mybrush, mycanvas, a ,22.5 , a);
     a = a (+) 1
};

```
### Program execution:

To execute the program, the AST is traversed and each node is evaluated. The *visitor pattern* was used to visit the AST nodes and execute the code corresponding to its operation in the Python programming language, mainly supported by the `Turtle` module.
## Compiler Architecture
### Lexer:

For lexical analysis, the ``lex`` module of the Python ``ply`` library was used.
Language reserved words and regular expressions were defined to recognize the tokens. To work with regular expressions the ``re`` library is used.
The ``#`` character was used to indicate the comment and the ``;`` character was used to indicate the end of an instruction.

### Parser:

For the parsing process, the ``yacc`` module of the Python ``ply`` library was used and the semantic rules were defined to indicate the semantic behavior of the language and the construction of the abstract syntax tree (AST). Yacc uses a LALR parser. Each grammar rule is specified as a ``Python`` function where the function docstring indicates the corresponding grammar rule. The file ``parsing.out`` shows how the grammar and the corresponding LALR automaton look.

### Semantic verification:

For the semantic verification phase, the visitor pattern was used to visit the AST nodes and perform the corresponding type checking, and other semantic type verifications. All semantic errors that the file may have are found and displayed together at the end.

Below are some semantic rules of the language:
- In the declaration or assignment of a variable, the type must match the static type with which the variable was named.
- The assignment or call to a variable can only be done on previously defined variables
- Two variables cannot have the same name.
- When calling a function, all its arguments must be passed in the same order in which the parameters were defined in the declaration.
- The condition of an ``if`` statement must be of type ``bool``
- The ``==`` operation is defined for operands of the same type. `

**Keywords**: vscode-extension, lsystem, compiler.