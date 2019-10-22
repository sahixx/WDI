def hashJoin(a1; a2; key):
  def akey: key | if type == "string" then . else tojson end;
  def wrap: { (akey) : . } ;
  # hash phase:
  (reduce a1[] as $o ({};  . + ($o | wrap ))) as $h1
  | (reduce a2[] as $o 
      ( {};
        ($o|akey) as $v
        | if $h1[$v] then . + { ($v): $o } else . end )) as $h2
  # join phase:
  | reduce ($h2|keys[]) as $key
      ([];  . + [ $h1[$key] + $h2[$key] ] ) ;

hashJoin($f1; $f2; .url)[]