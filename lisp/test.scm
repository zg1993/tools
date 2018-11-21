(define (p1) (p1))

(define (test predicate)
  (if predicate
      (p1)
      'hello))

(define (new-if predicate then-cluase else-cluase)
  (cond (predicate then-cluase)
	(else else-cluase)))
