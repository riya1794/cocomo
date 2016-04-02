The Constructive Cost Model (COCOMO) is an algorithmic software cost estimation model developed by Barry W. Boehm. The model uses a basic regression formula with parameters that are derived from historical project data and current as well as future project characteristics.


Basic COCOMO compute software development effort (and cost) as a function of program size. Program size is expressed in estimated thousands of source lines of code (SLOC, KLOC).

COCOMO applies to three classes of software projects:

Organic projects - "small" teams with "good" experience working with "less than rigid" requirements
Semi-detached projects - "medium" teams with mixed experience working with a mix of rigid and less than rigid requirements
Embedded projects - developed within a set of "tight" constraints. It is also combination of organic and semi-detached projects.(hardware, software, operational, ...)
The basic COCOMO equations take the form

Effort Applied (E) = ab(KLOC)bb [ man-months ]
Development Time (D) = cb(Effort Applied)db [months]
People required (P) = Effort Applied / Development Time [count]

where, KLOC is the estimated number of delivered lines (expressed in thousands ) of code for project. 