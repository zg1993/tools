(define (sum2 a b c)
  (let ((m (min a b)))
    (let ((m (min m c)))
      (- (+ a b c) m))))
