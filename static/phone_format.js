function format(input) {
    let numbers = input.value.replace(/\D/g, '');
    let chars = {0: '(', 3: ') ', 6: '-'};
    input.value = '';
    for (let i = 0; i < numbers.length; i++) {
      input.value += (chars[i] || '') + numbers[i];
    }
}
