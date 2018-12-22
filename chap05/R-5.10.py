encoder, decoder = [chr((k+shift)%26 + ord("A")), chr((k+shift)%26 + ord("A")) for k in range(26)]
self._forward, self._backward="".join(encoder), "".join(decoder)

