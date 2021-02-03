; Lab 14: Final Review

(define (compose-all funcs)
  (define (f arr sum)
    (if (null? arr) sum
      (f (cdr arr) ((car arr) sum))
    )
  )
  (define (helper val)
    (f funcs val)
  )
  helper
)

(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? curr seen-so-far) #t)
          (else (pair-tracker (append seen-so-far `(,(car curr))) (cdr-stream curr))))
    )
  (pair-tracker `() s)
)

(define (contains? lst s)
  (cond ((or (null? lst) (null? s)) #f)
        ((= (car lst) (car s)) #t)
        (else (contains? (cdr-stream lst) s))
  )
)

