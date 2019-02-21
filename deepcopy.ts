const foo = {
        primary: 'red',
        deep: {
            yyy: 'asdf'
        }
}

const bar = {
        secondary: 'green'
}
function deepcopy<T>(o: T): T {
  return JSON.parse(JSON.stringify(o));
}

const baz = deepcopy({...foo,...bar});

console.log(baz);

baz.secondary = 'blue';
console.log(baz);
