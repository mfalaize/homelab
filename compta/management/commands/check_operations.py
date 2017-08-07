from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand

from compta.bank import get_bank_class
from compta.models import Compte


def check_operations():
    """Récupère les dernières opérations bancaires en ligne, inscrit les nouvelles en base et les envoie par mail"""
    comptes = Compte.objects.all()
    for compte in comptes:
        operations = compte.operation_set.all()
        bank_class = get_bank_class(compte.banque)
        has_changed = False

        with bank_class(compte.login, compte.mot_de_passe, compte.numero_compte) as bank:
            new_operations = bank.fetch_last_operations()
            new_solde = bank.fetch_balance()

        for new_operation in new_operations:
            found = False
            for operation in operations:
                if operation.date_operation == new_operation.date_operation and operation.libelle == new_operation.libelle:
                    found = True
                    break
            if not found:
                new_operation.compte = compte
                new_operation.save()
                has_changed = True

        if compte.solde != new_solde:
            compte.solde = new_solde
            compte.save()

        if not has_changed:
            mails = []
            for user in compte.utilisateurs.all():
                if user.email is not None:
                    mails.append(user.email)
            if len(mails) > 0:
                send_mail('[Homelab] De nouvelles opérations ont été mises à jour sur le compte {}{}'.format(compte.banque, compte.numero_compte), "",
                      settings.DEFAULT_FROM_EMAIL, mails)


class Command(BaseCommand):
    help = "Déclenche le script qui vérifie les nouvelles opérations bancaires et qui envoie des mails lorsqu'il y en a des nouvelles"

    def handle(self, *args, **options):
        check_operations()
