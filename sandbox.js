function isPalindrome(word, index = 0) {
    return word.length / 2 <= index ? true :
        word[index] !== word.slice(-index-1)[0] ? false :
        isPalindrome(word, index + 1);
}
console.log(isPalindrome('qwertyytrewq'));
console.log(isPalindrome('poiiiii'))

const _isPalindrome = (word, index = 0) => word.length / 2 <= index ? true : word[index] !== word.slice(-index-1)[0] ? false : _isPalindrome(word, index + 1);
console.log(_isPalindrome('qwertyytrewq')) // true
console.log(_isPalindrome('poiiiii')) // false