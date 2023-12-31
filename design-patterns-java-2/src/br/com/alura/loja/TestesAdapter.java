package br.com.alura.loja;

import java.math.BigDecimal;

import br.com.alura.loja.http.ApacheHttpAdapter;
import br.com.alura.loja.orcamento.ItemOrcamento;
import br.com.alura.loja.orcamento.Orcamento;
import br.com.alura.loja.orcamento.RegistroOrcamento;

public class TestesAdapter {

	public static void main(String[] args) {

		int i = 010;
		int j = 07;

		System.out.println(i);
		System.out.println(j);
		Orcamento orcamento = new Orcamento();
		orcamento.adicionarItem(new ItemOrcamento(BigDecimal.TEN));
		orcamento.aprovar();
		orcamento.finalizar();

		RegistroOrcamento registro = new RegistroOrcamento(new ApacheHttpAdapter());
		registro.registrar(orcamento);
	}

}
