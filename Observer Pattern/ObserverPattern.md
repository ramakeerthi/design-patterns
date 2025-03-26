The Observer Pasttern:

    Defines a one-to-many dependency between objects so that
    when one object changes state, all of its dependents are
    notified and updated automatically.

-   PUBLISHER/SUBJECT + SUBSCRIBER/OBSERVER = OBSERVER PATTERN

-   Think of it like a magazine subscription, once you subscribe you get the latest issues
    as soon as they are released as long as you are subscribed. However, when you stop
    your subscription, you will not get any more issues however other subscribers will continue
    to get magazines.

-   The Subject contains the state and controls it, so there is one SUBJECT with state. The Observers,
    however use the state even though they don't own it. There can be many observers hence the ONE-TO-MANY
    relationship.


