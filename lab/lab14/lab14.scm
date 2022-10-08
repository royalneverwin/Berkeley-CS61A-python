(define (split-at lst n) 
    (define(func lst n) 
        (if (eq? n 0) nil
            (if (eq? lst nil) nil
                (cons (car lst) (func (cdr lst) (- n 1)))
                )
            )
        )
    (define (rest lst n)
        (if (eq? n 0) lst
            (if (eq? lst nil) nil
                (rest (cdr lst) (- n 1))
                )
            )
        )
    (cons (func lst n) (rest lst n))
)

(define (compose-all funcs) 
    (define (f x)
        (if (eq? funcs nil) x
            ((compose-all (cdr funcs)) ((car funcs) x))
            )
        )
    f
    )    
