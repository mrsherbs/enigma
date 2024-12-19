// Transcrypt'ed from Python, 2024-12-18 23:04:57
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, _sort, abs, all, any, assert, bin, bool, bytearray, bytes, callable, chr, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, hex, input, int, isinstance, issubclass, len, list, map, max, min, object, oct, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = '__main__';
export var plugboard = dict ({'A': 'M', 'M': 'A', 'F': 'G', 'G': 'F', 'H': 'Z', 'Z': 'H', 'K': 'L', 'L': 'K', 'Q': 'R', 'R': 'Q', 'U': 'T', 'T': 'U'});
export var offset_letter = function (letter, offset) {
	var start = ord ('A');
	var offset = __mod__ ((ord (letter) - start) + offset, 26);
	return chr (start + offset);
};
export var letter_to_alphabet_position = function (letter) {
	return (ord (letter) - ord ('A')) + 1;
};
export var swap = function (letter) {
	return plugboard.py_get (letter, letter);
};
export var alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
export var BETA = 'LEYJVCNIXWPBQMDRTAKZGFUHOS';
export var GAMMA = 'FSOKANUERHMBTIYCWLQPZXVGJD';
export var I = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ';
export var II = 'AJDKSIRUXBLHWTMCQGZNPYFVOE';
export var III = 'BDFHJLCPRTXVZNYEIWGAKMUSQO';
export var IV = 'ESOVPZJAYQUIRHXLNFTGKDCMWB';
export var V = 'VZBRGITYUPSDNHLXAWMJQOFECK';
export var VI = 'JPGVOUMFYQBENHZRDKASXLICTW';
export var VII = 'NZJHGRCXMYSWBOUFAIVLPEKQDT';
export var VIII = 'FKQHTLXOCBJSPDZRAMEWNIUYGV';
export var UKW_B = 'ENKQAUYWJICOPBLMDXZVFTHRGS';
export var UKW_C = 'RDOBJNTKVEHMLFCWZAXGYIPSUQ';
export var betaPosition = letter_to_alphabet_position ('A');
export var gammaPosition = letter_to_alphabet_position ('A');
export var rotorIPos = letter_to_alphabet_position ('A');
export var rotorIIPos = letter_to_alphabet_position ('A');
export var rotorIIIPos = letter_to_alphabet_position ('Z');
export var rotorIVPos = letter_to_alphabet_position ('A');
export var rotorVPos = letter_to_alphabet_position ('A');
export var rotorVIPos = letter_to_alphabet_position ('A');
export var rotorVIIPos = letter_to_alphabet_position ('A');
export var rotorVIIIPos = letter_to_alphabet_position ('A');
export var betaStellung = 1;
export var gammaStellung = 1;
export var rotorIStellung = 1;
export var rotorIIStellung = 1;
export var rotorIIIStellung = 1;
export var rotorIVStellung = 1;
export var rotorVStellung = 1;
export var rotorVIStellung = 1;
export var rotorVIIStellung = 1;
export var rotorVIIIStellung = 1;
export var rotorITurnover = new set ([letter_to_alphabet_position ('Z'), letter_to_alphabet_position ('M')]);
export var rotorIITurnover = new set ([letter_to_alphabet_position ('Z'), letter_to_alphabet_position ('M')]);
export var rotorIIITurnover = new set ([letter_to_alphabet_position ('Z'), letter_to_alphabet_position ('M')]);
export var rotorIVTurnover = new set ([letter_to_alphabet_position ('Z'), letter_to_alphabet_position ('M')]);
export var rotorVTurnover = new set ([letter_to_alphabet_position ('Z'), letter_to_alphabet_position ('M')]);
export var rotorVITurnover = new set ([letter_to_alphabet_position ('Z'), letter_to_alphabet_position ('M')]);
export var rotorVIITurnover = new set ([letter_to_alphabet_position ('Z'), letter_to_alphabet_position ('M')]);
export var rotorVIIITurnover = new set ([letter_to_alphabet_position ('Z'), letter_to_alphabet_position ('M')]);
export var rotorI = dict ({'RotorMap': I, 'Position': rotorIPos, 'Stellung': rotorIStellung, 'Turnover': rotorITurnover});
export var rotorII = dict ({'RotorMap': II, 'Position': rotorIIPos, 'Stellung': rotorIIStellung, 'Turnover': rotorIITurnover});
export var rotorIII = dict ({'RotorMap': III, 'Position': rotorIIIPos, 'Stellung': rotorIIIStellung, 'Turnover': rotorIIITurnover});
export var rotorIV = dict ({'RotorMap': IV, 'Position': rotorIVPos, 'Stellung': rotorIVStellung, 'Turnover': rotorIVTurnover});
export var rotorV = dict ({'RotorMap': V, 'Position': rotorVPos, 'Stellung': rotorVStellung, 'Turnover': rotorVTurnover});
export var rotorVI = dict ({'RotorMap': VI, 'Position': rotorVIPos, 'Stellung': rotorVIStellung, 'Turnover': rotorVITurnover});
export var rotorVII = dict ({'RotorMap': VII, 'Position': rotorVIIPos, 'Stellung': rotorVIIStellung, 'Turnover': rotorVIITurnover});
export var rotorVIII = dict ({'RotorMap': VIII, 'Position': rotorVIIIPos, 'Stellung': rotorVIIIStellung, 'Turnover': rotorVIIITurnover});
export var ukw_b = dict ({'RotorMap': UKW_B});
export var ukw_c = dict ({'RotorMap': UKW_C});
export var beta = dict ({'RotorMap': BETA, 'Position': betaPosition, 'Stellung': betaStellung});
export var gamma = dict ({'RotorMap': GAMMA, 'Position': gammaPosition, 'Stellung': gammaStellung});
export var bruh = function (input, rotor) {
	print (input);
	var py_new = offset_letter (input, (rotor ['Position'] - 1) + -(rotor ['Stellung'] - 1));
	print (py_new);
	var py_new = rotor ['RotorMap'] [alphabet.find (py_new)];
	print (py_new);
	var py_new = offset_letter (py_new, -((rotor ['Position'] - 1) + -(rotor ['Stellung'] - 1)));
	print (py_new);
	return py_new;
};
export var bruh_rev = function (input, rotor) {
	var py_new = offset_letter (input, (rotor ['Position'] - 1) + -(rotor ['Stellung'] - 1));
	var py_new = alphabet [rotor ['RotorMap'].find (py_new)];
	var py_new = offset_letter (py_new, -((rotor ['Position'] - 1) + -(rotor ['Stellung'] - 1)));
	return py_new;
};
export var word = '';
for (var letter of 'SIGMA') {
	print ('LETTER:', letter);
	if (letter.isalpha ()) {
		var letter = str.upper (letter);
		var letter = swap (letter);
		rotorIII ['Position'] = rotorIII ['Position'] + 1;
		if (rotorIII ['Position'] > 26) {
			rotorIII ['Position'] = 1;
		}
		if (rotorIII ['Position'] == rotorIII ['Turnover']) {
			rotorIII ['Position'] = rotorIII ['Position'] + 1;
		}
		if (rotorII ['Position'] > 26) {
			rotorII ['Position'] = 1;
		}
		if (rotorII ['Position'] == rotorIII ['Turnover']) {
			rotorII ['Position'] = rotorII ['Position'] + 1;
			rotorI ['Position'] = rotorI ['Position'] + 1;
		}
		if (rotorI ['Position'] > 26) {
			rotorI ['Position'] = 1;
		}
		if (rotorII ['Position'] > 26) {
			rotorII ['Position'] = 1;
		}
		var letter = bruh (letter, rotorIII);
		var letter = bruh (letter, rotorII);
		var letter = bruh (letter, rotorI);
		var letter = bruh (letter, beta);
		var letter = ukw_b ['RotorMap'] [alphabet.find (letter)];
		var letter = bruh_rev (letter, beta);
		var letter = bruh_rev (letter, rotorI);
		var letter = bruh_rev (letter, rotorII);
		var letter = bruh_rev (letter, rotorIII);
		var py_new = swap (letter);
	}
	else {
		var py_new = letter;
	}
	var word = word + py_new;
}
print (word);

//# sourceMappingURL=hello.map