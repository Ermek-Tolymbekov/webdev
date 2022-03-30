def cigar_party(cigars, is_weekend):
  if cigars >= 40:
    return is_weekend or cigars <= 60
  else:
    return False