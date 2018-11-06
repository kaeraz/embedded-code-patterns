*****************************
Embedded system documentation
*****************************

----------
Background
----------

In all my years as a programmer I participated in several huge embedded
software projects. A huge project, in my view, stands for a multi-board project
with many of variants e.g. board to board combinations, that development lasts
over a year or two. This kind of projects involve several software teams,
dedicated separately to each board, group of requirement engineers, and bunch
of other people, and finally, so called managers...

Working in such project and environment:

- Requires expensive complexity management
- Requires multi-level system engineering
- Suffers from communication and synchronization issues between the teams
- Needs constant and proper contractor-customer communication
- Depends on customer product specification maturity
- Requires good **systems**, **subsystems** and **code documentation**

There are many reasons why such a project may fail, get abandoned or rejected.
Most of the IT projects does not succeed in terms of time and money. However,
I do not want to yammer about a project issues, my todays goal is to elaborate
a bit on software development **documentation**.

System software documentation
-----------------------------

At the project initial stage selected people work on **SW architecture**.
There is no one definition of what **system architecture** is.

  *Architecture describes the basic organization of a system. It is embodied by
  its individual parts and their relations between each other and to their
  environment, as well as by the guidelines that manage the design and the
  development of the system.*

  -- IEEE Standard 1471

In general **software architecture** is about:

  - decomposing the system into parts called components, modules, elements
  - defining links between the parts by the means of interfaces

    + internal interfaces (inside the developed system)
    + external interfaces (for communication with outside world and environment)

  - describing SW components tasks, functions and responsibilities
  - presenting components interactions in functional view

Decomposition view
------------------
In this section I would like to elaborate a bit on several aspects of the
system architecture's **decomposition view**. **Decomposition view** presents
decomposed system - its parts, components, elements and modules. Lets discuss
simple example of two boards:

  - User interface board (**UI**)
  - Power board (**PB**)

The **UI** board is kind of GUI that contains display and buttons. In case of
washing machines **UI** board typically contains buttons, jog or rotator for
program selection (that can be illuminated) and a display e.g. LCD or LED version.
It is located at the top panel of the washing machine - everyone probably saw it...
The **PB** board contains all drivers required for washing machine operation such
as motor control driver, valves driver, heater driver, etc. By the driver I mean
electronic circuitries for driving the certain actuator (motor, valve, heater).

This kind of two board solution is a typical embedded system example. Lets
think a bit what both boards firmwares should look like. In my experience it
is a good approach to make **UI** board totally *stupid*. It means that
all the business logic and data management shall be located on the **PB** board.
This solution has one huge advantage - if there is a change in logic required
only **PB**'s firmware has to be updated and analogously if data presentation
change is requested only **UI**'s firmware is update. This is not always true
because it is usually hard to completely decouple both boards' software. In the
previous sentence is a small cheat. There is another big reason for this kind of solution
and it is an ability to change the **UI** board with different one (maybe another variant,
with some extra LEDs). Now, we have the same interface to both boards **UI_1**
and **UI_2** so that **UI's** firmware can only focus on data presentation.

**Footnote**

**kaeraz**, 2018/11
